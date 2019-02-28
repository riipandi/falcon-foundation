#!/usr/bin/env python3

import os, redis, whois
from falcon import falcon

class WhoisResource:
    def on_get(self, req, resp, domain):
        r = redis.Redis(host=str(os.getenv('REDIS_HOST')), port=os.getenv('REDIS_PORT'), db=0)
        w = whois.whois(domain)
        check = r.get(domain)

        if check:
            content = check
        else:
            r.set(domain, w.text + '!loaded from cache!')
            r.expire(domain, 3600)
            content = w.text

        resp.body = content
        resp.status = falcon.HTTP_200
