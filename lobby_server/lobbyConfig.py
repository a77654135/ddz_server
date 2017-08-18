from tornado.options import options,define

define("ipAddr","127.0.0.1",str,"lobby_server's ip address...")
define("ipPort",9000,int,"lobby_server's port...")
define("appName","ddz",str,"your app name.")