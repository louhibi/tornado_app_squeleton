#!/usr/bin/python

##Tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.autoreload
from tornado.options import options, define

##others
import traceback
import torndb
import logging

##internal imports
from myApp.app import MyApplication
from myApp1.app import MyApplication1




def main():
    try:
        """
        defining/parsing the options
        """
        define("port", default=8080, help="run on the given port", type=int)
        define("port1", default=8081, help="run on the given port", type=int)
        define("debug", default=False, help="run in debug mode", type=bool)
        tornado.options.parse_command_line()        
        logging.debug(options.logging)
        """
        initalising applications
        """ 
        app = MyApplication(options)
        app1 = MyApplication1(options)

        """
        starting tornado server
        """
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.listen(options.port)
        http_server1 = tornado.httpserver.HTTPServer(app1)
        http_server1.listen(options.port1)
        ioloop = tornado.ioloop.IOLoop.instance()
        tornado.autoreload.add_reload_hook(app.reloadTasks)
        tornado.autoreload.add_reload_hook(app1.reloadTasks)
        tornado.autoreload.start(ioloop)
        ioloop.start()

    except KeyboardInterrupt:
        pass
    except:
        print traceback.format_exc()


if __name__ == '__main__':
    main()