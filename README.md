# lokitoy

A script for reproducing some out-or-order peculiarities in loki.

## Usage

1. Clone this repo

2. Install requirements

```
your-favourite-package-manager install snappy
pip3 install -r requirements.txt
```

3. Run loki locally

```
git clone git@github.com:grafana/loki.git
cd loki/procution
docker-compose pull
docker-compose up
```

4. Run lokitoy

```
python3 lokitoy.py
```

5. Watch the world burn

```
CHUNK: {(...)}, RESULT: <Response [400]>, RESULT TEXT: entry out of order for stream: {app="m", uniq0="0", uniq1="0"}
```

## Documentation

Check out the documentation comments in [lokitoy.py](./lokitoy.py) - they are quite extensive!

## Some findings

* Using multiple shared labels of the form `"sharedN": ["random", "words", "here"]` doesn't seem to result in errors,
but including `"app": ['h', 'i', 'j', 'k', 'l', 'm']` in addition to those results in errors.
* If you use `['a', 'b', 'c', 'd', 'e', 'f']`, `["foo", "bar", "baz", "beep", "boop", "boom"]` or `["lokitest"]` as the selection for the `"app"` shared label,
the errors don't seem to happen, but when you use `['h', 'i', 'j', 'k', 'l', 'm']`, the errors do happen
