# -*- coding: utf-8 -*-
import requests
import logging

log = logging.getLogger(__name__)


class BaseAction(object):

    def do(self):
        raise NotImplementedError('Method need to be implement"')

    def json_data(self):
        raise NotImplementedError()


class Callback(BaseAction):

    def do(self):
        try:
            url = self.url_callback()
            json = self.json_data()
            requests.post(url, data=json)
        except Exception, e:
            log.error("Erro calling back")
            log.error(e)

    def url_callback(self):
        raise NotImplementedError()


class Counter(BaseAction):
    pass
