# coding:utf-8

import tornado.web

class WorkHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def post(self):
        self.application.pushToWorkThread(self)

    def process(self):
        msg = self.request.body
        print r'get message:  {0}'.format(msg)