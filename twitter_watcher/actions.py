# -*- coding: utf-8 -*-
import requests
import logging

log = logging.getLogger(__name__)


class Callback(object):

    def send(self):
        try:
            url = self.url_callback()
            json = self.json_data()
            requests.post(url, data=json)
        except Exception, e:
            log.error("Erro calling back")
            log.error(e)

    def url_callback(self):
        raise NotImplementedError()

    def json_data(self):
        raise NotImplementedError()
