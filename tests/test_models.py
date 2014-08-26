# -*- coding: utf-8 -*-
import unittest

from mongoengine import Document
from mongoengine.fields import ListField, StringField, DateTimeField
from twitter_watcher.db import Listener



class ListernerModel(unittest.TestCase):

	def test_subclass_document(self):
		assert issubclass(Listener, Document)

	def test_has_field_usernames(self):
		assert hasattr(Listener, 'usernames')
		assert isinstance(Listener.usernames, ListField)

	def test_has_field_hashtags(self):
		assert hasattr(Listener, 'hashtags')
		assert isinstance(Listener.hashtags, ListField)

	def test_has_field_start_date(self):
		assert hasattr(Listener, 'start_date')
		assert isinstance(Listener.start_date, DateTimeField)

	def test_has_field_end_date(self):
		assert hasattr(Listener, 'end_date')
		assert isinstance(Listener.end_date, DateTimeField)


