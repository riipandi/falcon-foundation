import os, falcon
from dotenv import load_dotenv
from pathlib import Path
from falcon_marshmallow import Marshmallow

# Import the resources
from resources import *

# Load dotenv
load_dotenv(dotenv_path = Path('.') / '.env')

# Handle 404
def handle_404(req, resp):
    resp.status = falcon.HTTP_404
    # resp.body = 'Resource not found'
    resp.media = {
        'status': falcon.HTTP_NOT_FOUND,
        'message': 'Resource not found',
        'documentation_url': 'https://github.com/riipandi/falcon-foundation',
    }

# falcon.API instances are callable WSGI apps
app = falcon.API(middleware=[Marshmallow()])

# things will handle all requests to the '/things' URL path
app.add_route('/', WelcomeResource())
app.add_route('/user', UserResource())
app.add_route('/static', StaticResource())

app.add_sink(handle_404, '')
