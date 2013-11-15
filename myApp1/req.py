#!/usr/bin/python

##imports
import traceback
import logging

##tornadoHelper imports
from tornadoHelper.extend import BaseHandler

class MainHandler(BaseHandler):
    pass

class indexHandler(MainHandler):
    def get(self):
        self.write("Using Tornado_app_squeleton")