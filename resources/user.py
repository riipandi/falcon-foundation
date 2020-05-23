from falcon import falcon

class UserResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.media = {
            'message': 'Welcome from User Resources',
            'works': ['The Stranger', 'The Myth of Sissyphus'],
            'status': 200,
        }
        resp.status = falcon.HTTP_200
