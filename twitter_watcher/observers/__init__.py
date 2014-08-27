# -*- coding: utf-8 -*-
import requests

__all__ = ['twitter']


class CallBack(object):

    def run(self):
        url = self.url_callback()
        json = self.json_data()
        requests.post(url, data=json)
        pass

    def json_data(self):
        raise NotImplementedError()

    def url_callback(self):
        raise NotImplementedError()
