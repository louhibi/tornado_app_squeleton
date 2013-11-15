#!/usr/bin/python

##tornadoHelper imports
from tornadoHelper.extend import ExtentedApplication
from tornadoHelper.url import Url
from myApp1.req import *


class MyApplication1(ExtentedApplication):

    def __init__(self, options):
        self.settings = dict(debug=options.debug, gzip=True,)
        self.urls = Url.get_urls()
        super(MyApplication1, self).__init__(self.urls, self.settings)

    def urls(self):
        pass


