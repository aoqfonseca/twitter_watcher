# -*- coding: utf-8 -*-
import unittest

from twitter_watcher import schema


class SchemaTestCase(unittest.TestCase):

    def test_return_true_for_valid_json(self):
        json = {'usernames': ['@aoqfonseca'],
                'hashtags': ['#testing'],
                'callback': "http://globo.com",
                'type': "CALLBACK",
                'startDate': '20140101T00:00',
                'endDate': '20140101T00:00'}

        assert schema.valid_json_listener(json)


    def test_return_false_for_type_diferent_of_string(self):
        json = {'usernames': ['@aoqfonseca'],
                'hashtags': ['#testing'],
                'callback': "http://globo.com",
                'type': 1,
                'startDate': '20140101T00:00',
                'endDate': '20140101T00:00'}
                
        assert schema.valid_json_listener(json) is False


    def test_return_false_for_required_fields(self):
        json = {'usernames': ['@aoqfonseca'],
                'callback': "http://globo.com",
                'startDate': '20140101T00:00',
                'endDate': '20140101T00:00'}

        assert schema.valid_json_listener(json) is False

        json = {'hashtags': ['#testing'],
                'callback': "http://globo.com",
                'startDate': '20140101T00:00',
                'endDate': '20140101T00:00'}

        assert schema.valid_json_listener(json) is False

        json = {'usernames': ['@aoqfonseca'],
                'callback': "http://globo.com",
                'hashtags': ['#testing'],
                'endDate': '20140101T00:00'}

        assert schema.valid_json_listener(json) is False

        json = {'usernames': ['@aoqfonseca'],
                'callback': "http://globo.com",
                'hashtags': ['#testing'],
                'startDate': '20140101T00:00'}

        assert schema.valid_json_listener(json) is False

        json = {'usernames': ['@aoqfonseca'],
                'hashtags': ['#testing'],
                'startDate': '20140101T00:00',
                'endDate': '20140101T00:00'}

        assert schema.valid_json_listener(json) is False

        json = {'usernames': ['@aoqfonseca'],
                'hashtags': ['#testing'],
                'callback': 'not valid callback',
                'startDate': '20140101T00:00',
                'endDate': '20140101T00:00'}

        assert schema.valid_json_listener(json) is False
