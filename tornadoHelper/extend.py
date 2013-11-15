#!/usr/bin/python

##Tornado
from tornado.web import Application, RequestHandler

## other
import logging
import traceback

class ExtentedApplication(Application):
    
    handlers = [] 

    def __init__(self, handlers, settings):        
        ## The settings of the application debug,logging,gzip
        try:
            logging.info("Starting application")
            # logging.debug("urls %s" % str(urls))
            # self.handlers.extend(urls)
            super(ExtentedApplication, self).__init__(handlers, **settings)
            # super(ExtentedApplication, self).__init__([], **settings)
        except:
            print traceback.format_exc()

    def reloadTasks(self):
        """ hook for tasks that apply before reloading :
            * closing connections to DBs
        """
        pass

class BaseHandler(RequestHandler):
    """
    The BaseHandler class inherit from tornado.web.RequestHandler
    \par
    Normally all handlers of the applications must inherit from the BaseHandler
    \par
    the base handler offer the authentication service to the authentication module

    \par Example:
    @code
    from Basehandler import BaseHandler
    class myHandler(BaseHandler):
        pass
    @endcode
    """
    pass
