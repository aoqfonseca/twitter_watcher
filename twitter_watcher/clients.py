# -*- coding: utf-8 -*-
from twitter_watcher.db.models import Listener


class TwitterClient(object):

    def __init__(self, app_key, app_secret, oauth_token, oauth_token_client):
        self.app_key = app_key
        self.app_secret = app_secret
        self.oauth_token = oauth_token
        self.oauth_token_client = oauth_token_client

    def get_all_listeners(self):
        self.listener = Listener.objects

    def build_usernames_set(self):
        usernames = [item.usernames for item in self.listener]
        return set(zip(*usernames))

    def build_hashtags_set(self):
        hashtags = [item.hashtags for item in self.listener]
        return set(zip(*hashtags))

    def start(self):
        pass

    def stop(self):
        pass

    def restart(self):
        self.start()
        self.stop()
