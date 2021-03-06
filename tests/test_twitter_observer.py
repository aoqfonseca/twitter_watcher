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

        observer.do = mock.MagicMock(return_value=True)
        observer.on_message(tweet)
        observer.do.assert_called_once_with()

    def test_dont_call_send_on_message(self):

        tweets = self.load_fixtures()
        tweet = tweets[0]

        observer = ObserverTwitter(url_callback='http://teste.com',
                                   usernames=['@aoqfonseca'],
                                   hashtags=[])

        observer.do = mock.MagicMock(return_value=True)
        observer.on_message(tweet)
        assert observer.do.call_count == 0

    def test_return_true_for_empty_user_list(self):
        tweets = self.load_fixtures()
        observer = ObserverTwitter(url_callback='http://test/com',
                                   usernames=[],
                                   hashtags=['test'])
        observer.tweet = tweets[0]

        self.assertTrue(observer.tweet_has_username())

    def test_return_true_for_empty_hashtags_list(self):
        tweets = self.load_fixtures()
        observer = ObserverTwitter(url_callback='http://test/com',
                                   usernames=['twitter'],
                                   hashtags=[])
        observer.tweet = tweets[0]

        self.assertTrue(observer.tweet_has_hashtags())
