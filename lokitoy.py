import itertools
import random
import random_words
import requests
import snappy as snappy
import time
import logproto_pb2
from google.protobuf import timestamp_pb2
import multiprocessing

def gen_uniq_label_sets(label_count, options_count):
    '''
    Creates tuples of the form ("uniqX", "N"), where 0 <= X < label_count and 0 <= N < options_count.
    Returns a cartesian product of these.
    No set of labels (=tuples) in the result is equal to another set of labels in the result.
    '''
    labels = []
    for i in range(label_count):
        labels.append([("uniq{}".format(i), str(j)) for j in range(options_count)])
    return list(itertools.product(*labels))

def build_chunk(shared_labels, uniq_labels, chunk_size, build_time):
    '''
    Builds a chunk that can be converted into a log stream for Loki.
    shared_labels should be a dict with list-of-strings values. The keys will be used as labels,
    and random choices made from the values are used as label values.
    uniq_labels should be a list of tuples. They will be included in each label set, with the first
    entry in each tuple being the label, and the second being the value.
    chunk_size should be an integer telling how many log entries there should be in the chunk.
    build_time should be a floating point value telling how long to sleep (in seconds) while building the chunk
    The chunk is a dict of form
    {
        '{app:"h",uniq1:"0",uniq2:"1"}': [
            {
                'ts': 1565785326.549417,
                'msg': 'the quick brown fox jumped over the lazy dog'
            },
            {
                'ts': 1565785377.3671732,
                'msg': 'hello world'
            }
        ],
        '{app:"j",uniq1:"0",uniq2:"1"}': [
            {
                'ts': 1565785429.616399,
                'msg': 'you can call me ishmael'
            }
        ]
    }
    The messages within each of the streams are guaranteed to be ordered by time,
    as they are appended to the lists with some sleeping in between and the ts is the timestamp at the time of appending.
    uniq1 and uniq2 in the example are the unique labels; they are always the same for all streams.
    '''
    # Split the build_time randomly into chunk_size parts - each part will be the sleeping time between consecutive log entries
    times = [build_time]
    while len(times) < chunk_size:
        index = random.randint(0, len(times) - 1)
        split = random.random()
        times = times[:index] + [times[index]*split, times[index]*(1-split)] + times[index+1:]

    chunk = {}
    rw = random_words.RandomWords()
    for t in times: #len(times) == chunk_size at this point
        time.sleep(t)
        labels = []

        # Generate random values for the shared labels of the log entry
        # For example, if shared_labels is {"hello": ["1", "2"], "world": ["a", "b"]},
        # this could result in 'hello="1"', 'world="b"'
        for k, v in shared_labels.items():
            labels.append("{}=\"{}\"".format(k, random.choice(v)))

        # Include the unique labels
        # For example, if the unique labels are [("uniq0", "0"), ("uniq1", "1")],
        # this will result in 'uniq0="0"', 'uniq1="1"'
        for k, v in uniq_labels:
            labels.append("{}=\"{}\"".format(k, v))

        # Join the labels into a key in the format that loki expects
        key = '{{{}}}'.format(','.join(labels))

        # Generate the actual log entry as a dict in the format of {"ts": <timestamp>, "msg": <message>}
        # and include it under the correct set of labels
        if key not in chunk:
            chunk[key] = []
        wordcount = random.randint(1, 20)
        chunk[key].append({"ts": time.time(), "msg": ' '.join(rw.random_words(count=wordcount))})

    return chunk
    

def chunk_to_push_request(chunk):
    '''
    Creates a PushRequest from a chunk created using build_chunk.
    A stream is created for each key in the chunk, and the key is used as labels,
    and entries are created for each item in the list under the given key.
    '''
    pr = logproto_pb2.PushRequest()
    for k, v in chunk.items():
        # Create a stream for each key
        stream = pr.streams.add()
        stream.labels = k

        for e in v:
            # Create a log entry for each item in the value
            entry = stream.entries.add()
            entry.line = e["msg"]
            entry.timestamp.seconds = int(e["ts"])
            entry.timestamp.nanos = round((e["ts"] - int(e["ts"])) * 1e9)

    return pr

def send_push_request(pr, dest):
    '''
    Serializes, compresses and sends the PushRequest (pr) to address (should be a loki's /api/prom/push-endpoint) given in dest
    '''
    return requests.post(dest, data=snappy.compress(pr.SerializeToString()))

def log_loop(params):
    '''
    Creates random chunks of logs, turns them into PushRequests and sends the PushRequests until terminated.
    Prints non-OK results (for example, and especially, out-of-order stuff) to stdout, along with the chunks that caused them.
    The params is a dictionary with entries as follows:
        min_build_time, max_build_time: float, minimum and maximum time to take to build each chunk, in seconds
        min_chunk_size, max_chunk_size: int, minimum and maxumum number of entries in each chunk
        shared_labels: dict of lists of strings, keys will be used as labels, and a random value is selected for the labels from the values
        uniq_labels: list of tuples of strings, the first entries in the tuples will be used as labels and the second entries as label values
        dest: string, the URL to send logs to
    '''
    while True:
        build_time = params["min_build_time"] + random.random()*(params["max_build_time"] - params["min_build_time"])
        chunk_size = random.randint(params["min_chunk_size"], params["max_chunk_size"])
        chunk = build_chunk(params["shared_labels"], params["uniq_labels"], chunk_size, build_time)
        pr = chunk_to_push_request(chunk)
        res = send_push_request(pr, params["dest"])
        if not res.ok:
            print("CHUNK: {}, RESULT: {}, RESULT TEXT: {}".format(chunk, res, res.text))

DEST = "http://localhost:3100/api/prom/push"
TIMEOUT = 60

if __name__ == '__main__':
    # 1. Create some unique label sets. For every process, this label set will be unique.
    # So, for example, with gen_uniq_label_sets(2, 2) there will be 4 processes.
    # Process 1 will have unique labels uniq0:"0",uniq1:"0", process 2 uniq0:"0",uniq1:"1",
    # process 3 uniq0:"1",uniq1:"0", and process 4 uniq0:"1",uniq1:"1".
    # Every process should therefore have an unique set of labels, and there shouldn't be any
    # out-of-order problems as long as each processes entries are in order.
    uniq_labels = gen_uniq_label_sets(2, 2)

    # 2. Create params for each label set. All other params except the unique labels are shared.
    params = [{
        "min_build_time": 1,
        "max_build_time": 3,
        "min_chunk_size": 5,
        "max_chunk_size": 10,
        "shared_labels": {"app": ['a', 'b', 'c', 'd', 'e', 'f']},
        "uniq_labels": u,
        "dest": DEST
    } for u in uniq_labels]

    # 3. Create a process for each set of params
    processes = [multiprocessing.Process(target=log_loop, args=(param,)) for param in params]

    # 4. Start the processes and watch loki go "400: entry out of order for stream"
    for p in processes:
        p.start()

    # 5. Kill everything after timeout (or after the first process fails for some reason)
    processes[0].join(TIMEOUT)
    for p in processes:
        p.terminate()
