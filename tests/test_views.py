# -*- coding: utf-8 -*-
import json
import unittest

from twitter_watcher import server


class ViewsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = server.api.test_client()

    def test_not_send_application_json_header(self):
        response = self.api.post('/listeners', data='not valid json')
        self.assertEquals(response.status_code, 406)

    def test_send_not_valid_json(self):
        response = self.api.post('/listeners',
                                 data='not valid json',
                                 content_type='application/json')

        self.assertEquals(response.status_code, 400)

    def test_error_for_invalid_parameter_callback(self):
        data = {'usernames': ['@aoqfonseca'],
                'hashtags': ['#testing'],
                'callback': "//globo.com",
                'startDate': '2014-01-01T00:00',
                'endDate': '2014-01-01T00:00'}

        data = json.dumps(data)

        response = self.api.post('/listeners',
                                 data=data,
                                 content_type='application/json')

        self.assertEquals(response.status_code, 400)

    def test_success_create_a_new_listener(self):
        data = {'usernames': ['@aoqfonseca'],
                'hashtags': ['#testing'],
                'callback': "http://globo.com",
                'startDate': '2014-01-01T00:00',
                'endDate': '2014-01-01T00:00'}

        data = json.dumps(data)

        response = self.api.post('/listeners',
                                 data=data,
                                 content_type='application/json')

        self.assertEquals(response.status_code, 201)

    def test_error_raise_for_invalid_data(self):
        data = {'usernames': ['@aoqfonseca'],
                'hashtags': ['#testing'],
                'callback': "http://globo.com",
                'startDate': 'aaaa',
                'endDate': '2014-01-01T00:00'}

        data = json.dumps(data)

        response = self.api.post('/listeners',
                                 data=data,
                                 content_type='application/json')

        self.assertEquals(response.status_code, 400)
