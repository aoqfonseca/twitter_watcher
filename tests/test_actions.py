# -*- coding: utf-8 -*-
import unittest
import mock

from twitter_watcher.actions import Callback


class CallbackActionTestCase(unittest.TestCase):

    def test_callback_has_method_send(self):
        assert hasattr(Callback, "send")
        assert callable(getattr(Callback, "send"))

    def test_callback_has_method_json_data(self):
        assert hasattr(Callback, "json_data")
        assert callable(getattr(Callback, "json_data"))

    def test_callback_has_method_url_callback(self):
        assert hasattr(Callback, "url_callback")
        assert callable(getattr(Callback, "url_callback"))

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

    @unittest.skip('not implemented')
    def test_callback_send_call_url_with_json_data(self):

        class FakeCallback(Callback):

            def json_data(self):
                return u'{"teste": "teste"}'

            def url_callback(self):
                return "http://teste.com"

        with mock.patch('twitter_watcher.actions.requests') as fake_requests:
            callback = FakeCallback()
            callback.send()
            fake_requests.\
                post.\
                assert_called_once_with(callback.url_callback(),
                                        data=callback.json_data())
