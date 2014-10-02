# -*- coding: utf-8 -*-
from twitter_watcher.db.models import Listener


class TwitterClient(object):

    def __init__(self, twitter_client=None):
        self.twitter_client = twitter_client

    def get_all_listeners(self):
        self.listener = Listener.objects

    def build_usernames_set(self):
        usernames = [item.usernames for item in self.listener]
        return set(zip(*usernames))

    def build_hashtags_set(self):
        hashtags = [item.hashtags for item in self.listener]
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
