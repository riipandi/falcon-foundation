import os
from falcon import falcon
from pathlib import Path

STATIC_DIR = str(Path('.').resolve()) + '/static'

# Static resource
class StaticResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open(STATIC_DIR + '/index.html', 'r') as f:
            resp.body = f.read()
