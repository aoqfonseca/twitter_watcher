# -*- coding: utf-8 -*-
import logging
import itertools

from twython import TwythonStreamer

log = logging.getLogger('stream_api')


class TwitterClient(object):

    def __init__(self, twitter_client=None, stream_client=None, listeners=[]):
        self.twitter_client = twitter_client
        self.stream_client = stream_client
        self.listeners = listeners

    def build_usernames_set(self):
        usernames = [item.usernames for item in self.listeners]
        usernames = itertools.chain(*usernames)
        return set(usernames)

    def build_hashtags_set(self):
        hashtags = [item.hashtags for item in self.listeners]
        hashtags = itertools.chain(*hashtags)
        return set(hashtags)

    def find_user_ids(self):
        usernames = self.build_usernames_set()
        usernames = map(lambda u: u.replace('@', ''), usernames)
        usernames = ",".join(usernames)
        users_ids = self.twitter_client.lookup_user(screen_name=usernames)
        users_ids = [item[u'id'] for item in users_ids]
        return users_ids

    def start(self):
        self.stream_client.listeners = self.listeners
        users = self.find_user_ids()
        users = ",".join(str(item) for item in users)

        hashtags = self.build_hashtags_set()
        hashtags = ",".join(hashtags)

        self.stream_client.statuses.filter(track=hashtags, follow=users)

    def stop(self):
        self.stream_client.disconnect()

    def restart(self):
        self.start()
        self.stop()


def call_listener(msg, listener):
    listener.on_message(msg)


class TwitterWatcherStream(TwythonStreamer):
    """ implementation of stream client """

    def on_success(self, data):
        log.debug("New message incoming. Lets call listeners [%s]", data)

    def on_error(self, status_code, data):
        log.error('Error stream api. STATUS %s . DATA %s',
                  status_code, data)
