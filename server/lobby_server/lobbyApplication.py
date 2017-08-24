#-.- coding:utf-8

import random
import tornado.web
from handlers.workHandler import WorkHandler
from tools.ColorLogger import getUZWLogger
from threadings.workThread import WorkThread

logger = getUZWLogger()

class LobbyApplication(tornado.web.Application):

    def __init__(self):
        handlers = [
            #工作线程执行器
            (r'/ddz/thread/', WorkHandler),
        ]
        tornado.web.Application.__init__(self,handlers=handlers)

    def startApplication(self):
        self.work_threads = []
        for i in range(0,4):
            t = WorkThread()
            self.work_threads.append(t)
            t.start()

    def stopApplication(self):
        for t in self.work_threads:
            t.pushToThread(None)
            t.join()
        self.work_threads = []

    def pushToWorkThread(self,handlerInst):
        t = random.choice(self.work_threads)
        t.pushToThread(handlerInst)