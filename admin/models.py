#!/usr/bin/env python
from google.appengine.ext import db


class Settings(db.Model):
    settingsJSON = db.TextProperty()
    backfilled = db.IntegerProperty(default=0)
    last_update = db.DateTimeProperty(auto_now_add=True, required=True)
