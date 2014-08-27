# -*- coding: utf-8 -*-

from twitter_watcher.actions import Callback


class ObserverTwitter(Callback):
	""" Listener/Observer for new tweet event """

	def __init__(self, *args, **kwargs):
		self.url = kwargs['url_callback']
		self.usernames = kwargs['usernames']
		self.hashtags = kwargs['hashtags']

		self.validate()

	def validate(self):
		if not isinstance(self.usernames, list):
			raise ValueError("usernames should be a list")

		if not isinstance(self.hashtags, list):
			raise ValueError("hashtags should be a list")

	def on_message(self, tweet):
		raise NotImplementedError()

	def json_data(self):
		return self.tweet

	def url_callback(self):
		return self.url
