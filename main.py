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




def main():
    try:
        """
        defining/parsing the options
        """
        define("port", default=8082, help="run on the given port", type=int)
        define("debug", default=False, help="run in debug mode", type=bool)
        tornado.options.parse_command_line()        
        logging.debug(options.logging)
        """
        initalising applications
        """ 
        app = MyApplication(options)

        """
        starting tornado server
        """
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.listen(options.port)
        ioloop = tornado.ioloop.IOLoop.instance()
        tornado.autoreload.add_reload_hook(app.reloadTasks)
        tornado.autoreload.start(ioloop)
        ioloop.start()

    except KeyboardInterrupt:
        pass
    except:
        print traceback.format_exc()


if __name__ == '__main__':
    main()