# -*- coding: utf-8 -*-

from twitter_watcher.actions import Callback


class ObserverTwitter(Callback):

    def __init__(self, **kwargs):
        self.url = kwargs['url_callback']
        self.usernames = kwargs['usernames']
        self.hashtags = kwargs['hashtags']

        self.validate()

    def tweet_has_username(self):
        screen_name = self.tweet.get('user').get('screen_name')
        screen_name = "@{}".format(screen_name)

        if not self.usernames:
            return True

        return screen_name in self.usernames

    def tweet_has_hashtags(self):
        hashtags = self.tweet.get('entities').get('hashtags')
        hashtags = [item['text'] for item in hashtags]

        intersection = [item for item in hashtags if item in self.hashtags]
        if not intersection and self.hashtags:
            return False

        return True

    def validate(self):
        if not isinstance(self.usernames, list):
            raise ValueError("usernames should be a list")

        if not isinstance(self.hashtags, list):
            raise ValueError("hashtags should be a list")

    def on_message(self, tweet):
        self.tweet = tweet

        if self.tweet_has_username() and self.tweet_has_hashtags():
            self.send()

    def json_data(self):
        return self.tweet

    def url_callback(self):
        return self.url
