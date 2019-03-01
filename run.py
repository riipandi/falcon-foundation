#!/usr/bin/env python3

import os
from falcon import falcon
from pathlib import Path
from app import *

BASE_DIR = Path('.').resolve()
ENV_PATH = BASE_DIR.joinpath('.env')

# Static resource
class StaticResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        page = str(Path('.').resolve()) + '/resources/index.html'
        with open(page, 'r') as f:
            resp.body = f.read()

# Handle 404
def handle_404(req, resp):
    resp.status = falcon.HTTP_404
    # resp.body = 'Resource not found'
    resp.media = {
        'message': 'Resource not found',
        'documentation_url': 'https://github.com/riipandi/falcon-foundation'
    }

api = falcon.API()

api.add_route('/', StaticResource())
# api.add_route('/', welcome.WelcomeResource())
api.add_route('/whois/{domain}', whois.WhoisResource())
api.add_sink(handle_404, '')
