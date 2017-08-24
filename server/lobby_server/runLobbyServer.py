# coding:utf-8

import lobbyConfig,lobbyApplication
import tornado.web
import tornado.ioloop
import tornado.httpserver
import time,signal,threading
from tornado.options import options
from tools.ColorLogger import getUZWLogger

keepRunning = True
serverApp = None
logger = None

'''
ddz 游戏入口
'''

def start_tornado():
    global serverApp
    serverApp = lobbyApplication.LobbyApplication()
    serverApp.startApplication()
    http_server = tornado.httpserver.HTTPServer(serverApp)
    http_server.listen(options.ipPort)
    logger.info(r"lobby server start on port:{0}".format(options.ipPort))
    tornado.ioloop.IOLoop.instance().start()


def stop_tornado():
    global keepRunning
    global serverApp
    serverApp.stopApplication()
    keepRunning = False

    lopper = tornado.ioloop.IOLoop.instance()
    lopper.add_callback(lambda x: x.stop(), lopper)
    logger.warning("ioloop shutdown...")
    pass


def main():
    global keepRunning
    global logger
    logger = getUZWLogger()
    tornado.options.parse_command_line()

    t = threading.Thread(target=start_tornado)
    t.start()

    signal.signal(signal.SIGINT,stop_tornado)
    signal.signal(signal.SIGTERM,stop_tornado)

    try:
        while keepRunning:
            time.sleep(1)
    except Exception,e:
        pass

    logger.warning("{0} stopped, bye.".format(options.appName))
    t.join()

if __name__ == '__main__':
    main()