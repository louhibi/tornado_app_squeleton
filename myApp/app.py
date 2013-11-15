#!/usr/bin/python

##tornadoHelper imports
from tornadoHelper.extend import ExtentedApplication
from myApp.req import indexHandler


class MyApplication(ExtentedApplication):

    def __init__(self, options):
        self.settings = dict(debug=options.debug, gzip=True,)
        # self.urls = Url.get_urls()
        self.handlers = [(r'/', indexHandler), ]
        super(MyApplication, self).__init__(self.handlers, self.settings)

    def urls(self):
        pass


