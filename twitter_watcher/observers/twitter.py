# -*- coding: utf-8 -*-

from twitter_watcher.actions import Callback


class ObserverTwitter(Callback):
	""" Listener/Observer for new tweet event """

	def on_message(self, tweet):
		raise NotImplementedError()

	def run(self):
		raise NotImplementedError()