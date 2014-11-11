# -*- coding: utf-8 -*-
import unittest
import mock

from twitter_watcher.actions import BaseAction, Callback, SaveTweet


class BaseActionTestCase(unittest.TestCase):

    def test_raise_error(self):
        try:
            base_action = BaseAction()
            base_action.do()
            assert False
        except NotImplementedError:
            assert True


class SaveTweetActionTestCase(unittest.TestCase):

    def test_callback_subclass(self):
        self.assertTrue(issubclass(SaveTweet, BaseAction))

    def test_action_has_method(self):
        self.assertTrue(hasattr(SaveTweet, "do"))
        self.assertTrue(callable(getattr(SaveTweet, "do")))

    def test_url_savetweet_raise_not_implemented(self):
        try:
            save_tweet_action = SaveTweet()
            save_tweet_action.url_callback()
            assert False
        except NotImplementedError:
            assert True

    def test_json_data_raise_not_implemented(self):
        try:
            save_tweet_action = SaveTweet()
            save_tweet_action.json_data()
            assert False
        except NotImplementedError:
            assert True

    def test_save_tweet_in_database(self):
        pass


class CallbackActionTestCase(unittest.TestCase):

    def test_callback_subclass(self):
        self.assertTrue(issubclass(Callback, BaseAction))

    def test_callback_has_method_send(self):
        self.assertTrue(hasattr(Callback, "do"))
        self.assertTrue(callable(getattr(Callback, "do")))

    def test_callback_has_method_json_data(self):
        self.assertTrue(hasattr(Callback, "json_data"))
        self.assertTrue(callable(getattr(Callback, "json_data")))

    def test_callback_has_method_url_callback(self):
        self.assertTrue(hasattr(Callback, "url_callback"))
        self.assertTrue(callable(getattr(Callback, "url_callback")))

    def test_url_callback_raise_not_implemented(self):
        try:
            callback = Callback()
            callback.url_callback()
            assert False
        except NotImplementedError:
            assert True

    def test_json_data_raise_not_implemented(self):
        try:
            callback = Callback()
            callback.json_data()
            assert False
        except NotImplementedError:
            assert True

    def test_callback_send_call_url_with_json_data(self):

        class FakeCallback(Callback):

            def json_data(self):
                return u'{"teste": "teste"}'

            def url_callback(self):
                return "http://teste.com"

        with mock.patch('twitter_watcher.actions.requests') as fake_requests:
            callback = FakeCallback()
            callback.do()
            fake_requests.\
                post.\
                assert_called_once_with(callback.url_callback(),
                                        data=callback.json_data())
