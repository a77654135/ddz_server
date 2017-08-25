#coding: utf-8

from tornado.options import options

def allowCrossDomain(func):
    def wrapper(*args,**kwargs):
        handler = args[0]
        if options.allow_crossdomain:
            handler.set_header('Access-Control-Allow-Origin', '*')

        try:
            ret = func(*args,**kwargs)
        except:
            ret = None
        return ret
    return wrapper