# -.-coding:utf-8

import threading
import Queue
#from tools.ColorLoggler im


#logger =

class BaseThread(threading.Thread):
    def __init__(self,name=None):
        self.dataQueue = Queue.Queue()
        self.name = name
        threading.Thread.__init__(self,name=name)

    def run(self):
        pass