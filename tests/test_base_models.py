# -*- coding: utf-8 -*-
import unittest

from twitter_watcher.db import BaseModel


class BaseModelTestCase(unittest.TestCase):

    def test_has_save_method(self):
        method = getattr(BaseModel, 'save')
        assert method is not None
        assert callable(method)

    def test_has_connect_database_method(self):
        method = getattr(BaseModel, 'connect_database')
        assert method is not None
        assert callable(method)

    def test_get_collection(self):

        class FakeDb(object):
            test = 'TestDbCollection'

        class TestClass(BaseModel):
            db_collection = "test"

            def connect_database(self):
                return FakeDb()

        test = TestClass()
        self.assertEquals(test.collection, 'TestDbCollection')
