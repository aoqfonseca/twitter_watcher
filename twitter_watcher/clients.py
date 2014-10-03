# -*- coding: utf-8 -*-
import logging
import functools

from multiprocessing import Pool

from twython import TwythonStreamer


class TwitterClient(object):

    def __init__(self, twitter_client=None, stream_client=None, listeners=[]):
        self.twitter_client = twitter_client
        self.stream_client = stream_client
        self.listeners = listeners

    def build_usernames_set(self):
        usernames = [item.usernames for item in self.listeners]
        return set(zip(*usernames))

    def build_hashtags_set(self):
        hashtags = [item.hashtags for item in self.listeners]
        return set(zip(*hashtags))

    def find_user_ids(self):
        usernames = self.build_usernames_set()
        usernames = map(lambda u: u.replace('@', ''), usernames)
        usernames = ",".join(usernames)
        return self.twitter_client.lookup_user(screen_name=usernames)

    def start(self):
        self.stream_client.listeners = self.listeners
        users = self.find_user_ids()
        users = ",".join(str(item) for item in users)

        hashtags = self.build_hashtags_set()
        hashtags = ",".join(hashtags)

        self.stream_client.filter(track=hashtags, follow=users)

    def stop(self):
        self.stream_client.disconnect()

    def restart(self):
        self.start()
        self.stop()


class TwitterWatcherStream(TwythonStreamer):
    """ implementation of stream client """

    log = logging.getLogger('stream_api')
    pool = Pool(5)

    def call_listener(self, listener, msg):
        listener.on_message(msg)

    def on_success(self, data):
        func = functools.partial(self.call_listener, data)
        self.pool.map(func, self.listeners)

    def on_error(self, status_code, data):
        self.log.error('Error stream api. STATUS %s . DATA %s',
                       status_code, data)
