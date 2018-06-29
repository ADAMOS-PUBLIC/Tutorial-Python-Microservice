# -*- coding: utf-8 -*-

import base64
import json
import logging
import os
import os
import pickle

import requests
import sys
import time
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

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.C8Y_HEADERS = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': self.request.headers.get('Authorization')}
        self.write(self.__get_devices())
      
    def __get_devices(self):
        response = requests.get(C8Y_BASE + '/inventory/managedObjects?fragmentType=c8y_IsDevice', headers=self.C8Y_HEADERS)
        return response.json()


def make_app():
    return tornado.web.Application([
        (r"/getdevices", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()

