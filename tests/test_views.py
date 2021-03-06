# -*- coding: utf-8 -*-
import json
import unittest
from datetime import datetime

from twitter_watcher import server
from twitter_watcher.db.models import Listener


class DetailViewListenerTestCase(unittest.TestCase):

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

    def test_return_json_listener(self):
        url = '/listener/{}'.format(self.listener.id)
        response = self.api.get(url)
        self.assertEquals(response.status_code, 200)
        expected = self.listener.to_json()
        returned = json.loads(response.data)
        self.assertEquals(returned['id'], expected['id']) 
        self.assertEquals(returned['usernames'], expected['usernames']) 
        self.assertEquals(returned['hashtags'], expected['hashtags']) 

    def test_400_for_invalid_object_id(self):
        url = '/listener/222222222222'
        response = self.api.get(url)
        self.assertEquals(response.status_code, 400)

    def test_404_for_not_found(self):
        url = '/listener/111111111111111111111111'
        response = self.api.get(url)
        self.assertEquals(response.status_code, 404)


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
                'callback': "//test.com",
                'type': "CALLBACK",
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
                         'callback': "http://test.com",
                         'type': "CALLBACK",
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
                'callback': "http://test.com",
                'type': "CALLBACK",
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
                         'callback': "http://test.com",
                         'type': "NEW TYPE",
                         'startDate': '2014-01-01T00:00',
                         'endDate': '2014-01-01T00:00'}

        data = json.dumps(listener_json)
        response = self.api.put('/listener/%s' % self.listener.id,
                                data=data,
                                content_type='application/json')

        self.assertEquals(response.status_code, 200)
        self.listener = Listener.objects.get(id=self.listener.id)

        # Checking if data is changed
        self.assertEquals(self.listener.usernames, listener_json['usernames'])
        self.assertEquals(self.listener.hashtags, listener_json['hashtags'])
        self.assertEquals(self.listener.type, listener_json['type'])

    def test_error_raise_for_invalid_data(self):
        data = {'usernames': ['@aoqfonseca'],
                'hashtags': ['#testing'],
                'callback': "http://globo.com",
                'type': "CALLBACK",
                'startDate': 'aaaa',
                'endDate': '2014-01-01T00:00'}

        data = json.dumps(data)

        response = self.api.put('/listener/%s' % self.listener.id,
                                data=data,
                                content_type='application/json')

        self.assertEquals(response.status_code, 400)


class DeleteListenerTestCase(unittest.TestCase):

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

    def test_delete(self):
        response = self.api.delete('/listener/%s' % self.listener.id,
                                   content_type='application/json')

        self.assertEquals(response.status_code, 200)
        listeners = Listener.objects.filter(id=self.listener.id)
        assert len(listeners) == 0


class ListAllListenersView(unittest.TestCase):

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

    def test_get_all_listeners(self):
        response = self.api.get('/listeners', content_type='application/json')
        self.assertEquals(response.status_code, 200)
        data = json.loads(response.data)
        listeners = data['listeners']
        self.assertEquals(len(listeners), 1)
        self.assertEquals(listeners[0]['usernames'], self.listener.usernames)
        self.assertEquals(listeners[0]['hashtags'], self.listener.hashtags)
        self.assertEquals(listeners[0]['id'], str(self.listener.id))
