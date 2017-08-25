# coding:utf-8

import sys
sys.path.append("../..")
import tornado.web
from decoratorBase import allowCrossDomain

class WorkHandler(tornado.web.RequestHandler):
    @allowCrossDomain
    @tornado.web.asynchronous
    def post(self):
        self.application.pushToWorkThread(self)

    def process(self):
        msg = self.request.body
        print r'get message:  {0}'.format(msg)
        return msg