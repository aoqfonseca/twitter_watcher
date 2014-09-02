# -*- coding: utf-8 -*-
import unittest

from twitter_watcher import server


class ViewsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = server.api.test_client()

    def test_not_send_application_json_header(self):
        response = self.api.post('/listeners', data='not valid json')
        self.assertEquals(response.status_code, 400)

    def test_send_not_valid_json(self):
        response = self.api.post('/listeners',
                                 data='not valid json',
                                 content_type='application/json')

        self.assertEquals(response.status_code, 405)
