# coding:utf-8

import tornado.web

class ThreadHandler(tornado.web.RequestHandler):
    def post(self):
        self.application