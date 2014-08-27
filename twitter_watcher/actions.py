# -*- coding: utf-8 -*-
import requests


class Callback(object):

    def send(self):
        url = self.url_callback()
        json = self.json_data()
        requests.post(url, data=json)

    def url_callback(self):
        raise NotImplementedError()

    def json_data(self):
        raise NotImplementedError()
