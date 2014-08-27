# -*- coding: utf-8 -*-
import unittest

from twitter_watcher import server


class ServerTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = server.api.test_client()

    def test_healthcheck(self):
        response = self.api.get('/healthcheck')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data, 'WORKING')
