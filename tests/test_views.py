# -*- coding: utf-8 -*-
import json
import unittest
from datetime import datetime

from twitter_watcher import server
from twitter_watcher.db.models import Listener


class CreateListenerViewsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = server.api.test_client()

    def tearDown(self):
        Listener.objects.all().delete()

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
        listener_json = {'usernames': ['@aoqfonseca'],
                         'hashtags': ['#testing'],
                         'callback': "http://globo.com",
                         'startDate': '2014-01-01T00:00',
                         'endDate': '2014-01-01T00:00'}

        data = json.dumps(listener_json)
        self.assertEquals(len(Listener.objects.all()), 0)

        response = self.api.post('/listeners',
                                 data=data,
                                 content_type='application/json')

        self.assertEquals(response.status_code, 201)

        listener = Listener.objects(callback=listener_json['callback']).first()

        self.assertEquals(listener.usernames, listener_json['usernames'])

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


class UpdateListenerTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = server.api.test_client()

    def setUp(self):
        self.listener = Listener(usernames=['@teste'],
                                 hashtags=['#123'],
                                 start_date=datetime.now(),
                                 end_data=datetime.now())
        self.listener.save()

    def tearDown(self):
        self.listener.delete()

    def test_update_with_success(self):
        listener_json = {'usernames': ['@aoqfonseca'],
                         'hashtags': ['#testing'],
                         'callback': "http://globo.com",
                         'startDate': '2014-01-01T00:00',
                         'endDate': '2014-01-01T00:00'}

        data = json.dumps(listener_json)
        response = self.api.put('/listener/%s' % self.listener.id,
                                 data=data,
                                 content_type='application/json')

        self.assertEquals(response.status_code, 204)
        self.listener = Listener.objects.get(id=self.listener.id)

        #Checking if data is changed
        self.assertEquals(self.listener.usernames, listener_json['usernames'])
        self.assertEquals(self.listener.hashtags, listener_json['hashtags'])

    def test_error_raise_for_invalid_data(self):
        data = {'usernames': ['@aoqfonseca'],
                'hashtags': ['#testing'],
                'callback': "http://globo.com",
                'startDate': 'aaaa',
                'endDate': '2014-01-01T00:00'}

        data = json.dumps(data)

        response = self.api.put('/listener/%s' % self.listener.id,
                                 data=data,
                                 content_type='application/json')

        self.assertEquals(response.status_code, 400)
