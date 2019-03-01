#!/usr/bin/env python3

import os, redis, whois
from falcon import falcon

class WhoisResource:
    def on_get(self, req, resp, domain):
        w = whois.whois(domain)
        content = w.text

        try:
            r = redis.from_url(os.getenv('REDIS_CONN'))
            check = r.get(domain)
            if check:
                content = check
            else:
                r.set(domain, w.text + '!loaded from cache!')
                r.expire(domain, 3600)
                content = w.text
        except redis.ConnectionError:
            content = 'Redis connection failed!'


        resp.body = content
        resp.status = falcon.HTTP_200
