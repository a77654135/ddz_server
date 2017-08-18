# coding:utf-8

import tornado.httpserver

class ThreadHandler(tornado.httpserver.HTTPRequest):
    def get(self):
        pass