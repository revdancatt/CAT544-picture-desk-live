#!/usr/bin/env python
from google.appengine.ext.webapp import template
from google.appengine.api import memcache
from admin.models import Settings
import webapp2
import json
import sys
import os


class MainHandler(webapp2.RequestHandler):
    def get(self):

        #   Default template values that we'll pass over
        template_values = {
            'status': 'ok',
            'msg': {'kittens': 23, 'puppies': 1}
        }

        #   We first need to see if we have the guardian
        #   api key in memcache...
        settingsJSON = memcache.get('settingsJSON')

        #   ...if we don't the apiKey in memcache then we
        #   will try and fetch it from the database...
        if settingsJSON is None:

            rows = Settings.all()

            #   If there isn't a database entry then we
            #   know that the thing hasn't been setup
            #   so we should send the user to the setup
            #   page
            if rows.count() == 0:
                path = os.path.join(os.path.dirname(__file__), 'templates/apiKey.html')
                self.response.out.write(template.render(path, template_values))
            else:
                row = rows[0]
                settingsJSON = json.loads(row.settingsJSON)
                memcache.set('settingsJSON', settingsJSON, 86400)  # 60s * 60m *24h

        #   Now that we have the settings file (and
        #   if we have a settings file we automatically
        #   have the api key, we need to look and see
        #   if we need to backfill the old Picture Desk
        #   Live blogs
        if settingsJSON is not None:
            self.response.write('Check backfill')


app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)
