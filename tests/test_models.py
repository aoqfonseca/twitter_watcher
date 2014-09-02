# -*- coding: utf-8 -*-
import unittest

from datetime import datetime

from mongoengine import connect
from mongoengine import Document
from mongoengine.fields import ListField, DateTimeField

from twitter_watcher.db.models import Listener
from twitter_watcher.observers import ObserverTwitter


class ListernerModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connect('twitter_watcher_test')

    def tearDown(self):
        Listener.objects.delete()

    def test_subclass_document(self):
        assert issubclass(Listener, Document)

    def test_subclass_action_callback(self):
        assert issubclass(Listener, ObserverTwitter)

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

    def test_create_a_listener(self):
        listener = Listener(usernames=['@teste1', '@teste2'],
                            hashtags=['#blabla', '#blabla2'],
                            start_date=datetime.now(),
                            end_date=datetime.now())

        assert listener.id is None
        listener.save()
        assert listener.id is not None

        # finding
        listener = Listener.objects(id=listener.id)[0]
        self.assertEquals(listener.usernames, ['@teste1', '@teste2'])
        self.assertEquals(listener.hashtags, ['#blabla', '#blabla2'])
