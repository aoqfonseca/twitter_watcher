# -*- coding: utf-8 -*-
import json
import unittest
import mock

from twitter_watcher.observers import ObserverTwitter
from twitter_watcher.actions import Callback


class TwitterObserverTestCase(unittest.TestCase):

    def load_fixtures(self):
        fixtures = open('tests/fixtures/tweets.json', 'r')
        twitter_json_list = json.load(fixtures)
        return twitter_json_list

    def test_subclass_of_action_callback(self):
        assert issubclass(ObserverTwitter, Callback)

    def test_have_a_on_message_method(self):
        assert hasattr(ObserverTwitter, 'on_message')
        assert callable(ObserverTwitter.on_message)

    def test_raise_value_error_for_username_not_a_list(self):
        try:
            ObserverTwitter(url_callback='http://teste.com',
                            usernames='',
                            hashtags=[])
            assert False
        except ValueError:
            assert True

    def test_raise_value_error_for_hashtags_not_a_list(self):
        try:
            ObserverTwitter(url_callback='http://teste.com',
                            usernames=[],
                            hashtags='tests')
            assert False
        except ValueError:
            assert True

    def test_send_message_to_callback_url(self):

        tweets = self.load_fixtures()
        tweet = tweets[0]

        observer = ObserverTwitter(url_callback='http://teste.com',
                                   usernames=['@twitterapi'],
                                   hashtags=[])

        observer.send = mock.MagicMock(return_value=True)
        observer.on_message(tweet)
        observer.send.assert_called_once_with()
