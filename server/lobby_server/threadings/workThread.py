# -.-coding:utf-8

import sys
sys.path.append("..")
import threading
import Queue
import tornado.ioloop
from tools.ColorLogger import getUZWLogger

logger = getUZWLogger()

class WorkThread(threading.Thread):

    THREAD_ID = 1

    def __init__(self,name=None):
        threading.Thread.__init__(self)
        self.dataQueue = Queue.Queue()
        self.name = r'[work_thread_{0}]'.format(WorkThread.THREAD_ID)
        WorkThread.THREAD_ID += 1
        logger.info(r"{0} start successfully......".format(self.name))

    def pushToThread(self,handlerInst):
        self.dataQueue.put(handlerInst)

    def finishHandler(self,handler,response):
        try:
            if response is None:
                handler.send_error(404)
            else:
                handler.finish(response)
        except Exception,e:
            handler.send_error(500)


    def run(self):
        while True:
            try:
                handlerInst = self.dataQueue.get(True,0.5)
            except Queue.Empty:
                continue

            if handlerInst is None:
                logger.warn(r"thread {0} get None, exit...".format(self.name))
                break

            try:
                response = handlerInst.process()
            except Exception,e:
                logger.error(r"thread {0} get error: {1}".format(self.name,e.message))
                response = None

            try:
                tornado.ioloop.IOLoop.instance().add_callback(self.finishHandler,handlerInst,response)
            except Exception,e:
                logger.error(r"thread {0} get error: {1}".format(self.name, e.message))

