# -*- coding: utf-8 -*-
import unittest

from twitter_watcher import schema


class SchemaTestCase(unittest.TestCase):

    def test_return_true_for_valid_json(self):
        json = {'usernames': ['@aoqfonseca'],
                'hashtags': ['#testing'],
                'startDate': '20140101T00:00',
                'endDate': '20140101T00:00'}

        assert schema.check_json_listener(json)

    def test_return_false_for_required_fields(self):
        json = {'usernames': ['@aoqfonseca'],
                'startDate': '20140101T00:00',
                'endDate': '20140101T00:00'}

        assert schema.check_json_listener(json) is False

        json = {'hashtags': ['#testing'],
                'startDate': '20140101T00:00',
                'endDate': '20140101T00:00'}

        assert schema.check_json_listener(json) is False

        json = {'usernames': ['@aoqfonseca'],
                'hashtags': ['#testing'],
                'endDate': '20140101T00:00'}

        assert schema.check_json_listener(json) is False

        json = {'usernames': ['@aoqfonseca'],
                'hashtags': ['#testing'],
                'startDate': '20140101T00:00'}

        assert schema.check_json_listener(json) is False
