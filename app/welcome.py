#!/usr/bin/env python3

from falcon import falcon

class WelcomeResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        result = {
            'title': 'Welcome to Falcon',
            'message': (
                "This is an example application."
            ),
            'author': 'Aris Ripandi <aris@ripandi.id>',
        }
        resp.media = result
