# -*- coding: utf-8 -*-
import logging

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
        pass

    def stop(self):
        pass

    def restart(self):
        self.start()
        self.stop()


class TwitterWatcherStream(TwythonStreamer):
    """ implementation of stream client """

    log = logging.getLogger('stream_api')

    def listeners(self, itens):
        self._listeners = itens

    def on_success(self, data):
        pass

    def on_error(self, status_code, data):
        self.log.error('Error stream api. STATUS %s . DATA %s',
                       status_code, data)
