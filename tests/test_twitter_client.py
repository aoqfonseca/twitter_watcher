# -*- coding: utf-8 -*-
import unittest
import datetime
from mock import MagicMock

from mongoengine import connect

from twitter_watcher.db.models import Listener
from twitter_watcher.clients import TwitterClient


class TwitterClientTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(clz):
        connect('twitter_watcher_test')
        now = datetime.datetime.now()
        seven_days_ago = now - datetime.timedelta(days=7)
        tomorrow = now + datetime.timedelta(days=1)

        clz.listener_a = Listener(usernames=['@twitter_api'],
                                  hashtags=['#test'],
                                  start_date=seven_days_ago,
                                  end_date=tomorrow)

        clz.listener_b = Listener(usernames=['@twitter_api', '@aoqfonseca'],
                                  hashtags=['#test', '#test2'],
                                  start_date=seven_days_ago,
                                  end_date=tomorrow)
        clz.listener_a.save()
        clz.listener_b.save()

    @classmethod
    def tearDownClass(clz):
        clz.listener_a.delete()
        clz.listener_b.delete()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_mount_a_set_with_usernames(self):
        client = TwitterClient()

        client.get_all_listeners()

        usernames_set = client.build_usernames_set()
        expected = zip(self.listener_a.usernames, self.listener_b.usernames)
        expected = set(expected)

        self.assertEquals(usernames_set, expected)

    def test_mount_a_set_with_hashtags(self):
        client = TwitterClient()

        client.get_all_listeners()

        hashtags_set = client.build_hashtags_set()
        expected = zip(self.listener_a.hashtags, self.listener_b.hashtags)
        expected = set(expected)

        self.assertEquals(hashtags_set, expected)

    def test_find_users_id_in_twitter(self):
        tw_client = MagicMock()
        tw_client.lookup_user.return_value = [{u'id': 12127898},
                                              {u'id': 12312334}]

        client = TwitterClient(tw_client)
        screen_names = ['@aoqfonseca', '@twitterapi']

        client.build_usernames_set = MagicMock(return_value=screen_names)
        client.find_user_ids()
        screen_names = map(lambda u: u.replace('@', ''), screen_names)
        screen_names = ",".join(screen_names)
        tw_client.lookup_user.assert_called_once_with(screen_name=screen_names)
