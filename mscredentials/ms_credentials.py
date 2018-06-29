# -*- coding: utf-8 -*-

import base64
import json
import logging
import os
import os
import sys
import time

import requests
import tornado.ioloop
import tornado.web

logging.basicConfig(level=logging.INFO)

logging.info(os.environ)

'''
Start configuration
'''
C8Y_BASE = os.environ.get('C8Y_BASEURL')
C8Y_TENANT = os.environ.get('C8Y_TENANT')
C8Y_USER = os.environ.get('C8Y_USER')
C8Y_PASSWORD = os.environ.get('C8Y_PASSWORD')

'''
End configuration
'''

logging.info(C8Y_BASE)
logging.info(C8Y_TENANT)
logging.info(C8Y_USER)
logging.info(C8Y_PASSWORD)
str = C8Y_TENANT + '/' + C8Y_USER + ':' + str(C8Y_PASSWORD)
logging.info(str)

C8Y_HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Basic ' + base64.b64encode(str.encode('utf-8')).decode()
}
#response = requests.get(C8Y_BASE + '/inventory/managedObjects?fragmentType=c8y_IsDevice', headers=C8Y_HEADERS)
#logging.info(response.json())

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write(self.__get_devices())

    def __get_devices(self):
        response = requests.get(C8Y_BASE + '/inventory/managedObjects?fragmentType=c8y_IsDevice', headers=C8Y_HEADERS)
        return response.json()


def make_app():
    return tornado.web.Application([
        (r"/devices", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()

