# -*- coding: utf-8 -*-
import unittest

from twitter_watcher.observers.twitter import ObserverTwitter
from twitter_watcher.actions import Callback


class TwitterObserverTestCase(unittest.TestCase):

	def test_subclass_of_action_callback(self):
		assert issubclass(ObserverTwitter, Callback)

	def test_have_a_on_message_method(self):
		assert hasattr(ObserverTwitter, 'on_message')
		assert callable(ObserverTwitter.on_message)

	def test_have_a_run(self):
		assert hasattr(ObserverTwitter, 'run')
		assert callable(ObserverTwitter.run)

	def test_on_message_raise_not_implemented_error(self):
		observer = ObserverTwitter()
		try:
			observer.on_message(None)
			assert False
		except NotImplementedError, error:
			assert True

	def test_run_raise_not_implemented_error(self):
		observer = ObserverTwitter()
		try:
			observer.run()
			assert False
		except NotImplementedError, error:
			assert True
