import os, falcon

class WelcomeResource(object):
    def on_get(self, req, resp):
        """req['result'] will be automatically serialized
            The key in which results are stored can be customized when
            the middleware is instantiated.
        """
        data = {
            'message': 'Welcome from Falcon',
            'environment': os.getenv("APP_ENV"),
            'debug': bool(os.getenv("APP_DEBUG")),
            'status': 200,
        }
        req.context['result'] = data
