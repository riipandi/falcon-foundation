# Falcon Foundation

A boilerplate for Falcon project.

[Falcon][falcon] is a reliable, high-performance Python web framework for building large-scale app backends and microservices. It encourages the REST architectural style, and tries to do as little as possible while remaining highly effective.

Falcon apps work with any WSGI server, and run like a champ under CPython 2.7, CPython 3.4+, PyPy2.7, and PyPy3.5.

## Quick Start

Preparing workspace:

```
cd /to/your/working/directory
virtualenv -qp python3 .venv --download
.venv/bin/pip install -r requirements.txt
```

Run the application:

```
.venv/bin/gunicorn run:api -c config/gunicorn.py
```

## License

This project is open-sourced software licensed under the [MIT license](./license.txt).


[falcon]:https://falconframework.org/
