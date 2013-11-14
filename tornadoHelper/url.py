import tornado.web
import logging


class Url(object):
    """
    A decorator that binds a handler to a route
    \par Example:
    @code
    @route("/listing/")
    class indexHandler(basehandler.baseHandler):
        pass
    @endcode
    """
    urls = []

    def __init__(self, uri, name=None):
        logging.debug("in Url init")
        self.uri = uri
        self.name = name

    def __call__(self, handler):
        """gets called when we class decorate"""
        name = self.name and self.name or handler.__name__
        self.urls.append(tornado.web.url(self.uri, handler, name=name))
        return handler

    @classmethod
    def get_urls(self):
        return self.urls