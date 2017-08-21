# coding:utf-8

import tornado.web

class WorkHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.application.pushToWorkThread(self)

    def process(self):
        name = self.get_argument("name","wc")
        return name