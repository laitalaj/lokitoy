from flask import Flask, request
import snappy
from sqlitedict import SqliteDict
import logproto_pb2
from google.protobuf import timestamp_pb2

app = Flask(__name__)
db = SqliteDict(':memory:', autocommit=True)

@app.route('/', methods=['GET', 'POST'])
def endpoint():
    '''
    A mock endpoint that receives snappied logprotos, just like loki,
    and checks that the label timestamps are in order.

    Run this with flask using:

    export FLASK_APP=lokimock.py
    flask run
    '''
    if request.method == 'GET':
        return 'Post some stuff here as you\'d post to loki'

    log = logproto_pb2.PushRequest()
    log.ParseFromString(snappy.uncompress(request.data))
    for stream in log.streams:
        labels = stream.labels
        if labels in db:
            current_ts = db[labels]
        else:
            print('Added labels: {}'.format(labels))
            current_ts = 0
        for entry in stream.entries:
            entry_ts = int(entry.timestamp.seconds * 1e9) + entry.timestamp.nanos
            if entry_ts <= current_ts:
                ooo_msg = 'OUT OF ORDER LOG DETECTED: Labels {}, Current ts: {}, Log\'s ts: {}'.format(labels, current_ts, entry_ts)
                print(ooo_msg)
                return ooo_msg, 400
            current_ts = entry_ts
        db[labels] = current_ts
    return 'ok :^)'
