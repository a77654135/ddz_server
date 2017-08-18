#-.- coding:utf-8

import tornado.web
from handlers import threadHandler
from tools.ColorLogger import getUZWLogger

logger = getUZWLogger()

class LobbyApplication(tornado.web.Application):
    def __init__(self):
        handlers = [
            #工作线程执行器
            (r'/ddz/thread/', threadHandler),
        ]
        tornado.web.Application.__init__(self,handlers=handlers)

    def startApplication(self):
        pass

    def stopApplication(self):
        pass