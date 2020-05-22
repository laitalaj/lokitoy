# lokitoy

A script for reproducing some out-or-order peculiarities in [loki](https://github.com/grafana/loki),
and a tiny flask app for making sure that the script works correctly.

**The guys at Loki eventually figured out that the out of order stuff was caused by a hash collision,
and this should be fixed as of the latest versions of Loki.
More info [here](https://github.com/grafana/loki/issues/898#issuecomment-552333246).**

## Usage

1. Clone this repo

2. Install requirements

```
your-favourite-package-manager install snappy
pip3 install -r requirements.txt
```

On macOS, you might encounter some errors with installing python-snappy - [this stackoverflow answer](https://stackoverflow.com/questions/11416024/error-installing-python-snappy-snappy-c-h-no-such-file-or-directory/41707800#41707800) might help you in that case!

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

Lokitoy now has some command line options! Try `python3 lokitoy.py --help` to see them.

## Checking that the script actually sends stuff in order

1. Make sure that you've installed the requirements

2. Set the `FLASK_APP` environment variable to point to `lokimock.py`
```
export FLASK_APP=lokimock.py
```

3. Run lokimock with flask
```
flask run
```

4. Run lokitoy with the `--mock` flag
```
python3 lokitoy.py --mock
```

5. Watch the world *not* burn

You can see that lokimock catches out-of-orders as it should by telling lokitoy to deliberately send stuff out-of-order:
```
python3 lokitoy.py --mock --deliberate-ooo
```

## Documentation

Check out the documentation comments in [lokitoy.py](./lokitoy.py) - they are quite extensive!

## Some findings

* Using multiple shared labels of the form `"sharedN": ["random", "words", "here"]` doesn't seem to result in errors,
but including `"app": ['h', 'i', 'j', 'k', 'l', 'm']` in addition to those results in errors.
* If you use `['a', 'b', 'c', 'd', 'e', 'f']`, `["foo", "bar", "baz", "beep", "boop", "boom"]` or `["lokitest"]` as the selection for the `"app"` shared label,
the errors don't seem to happen, but when you use `['h', 'i', 'j', 'k', 'l', 'm']`, the errors do happen
* If you rename the `"app"` shared label to `"test"`, there are no errors
