# -*- coding: utf-8 -*-
import logging

from flask.ext.script import Command
from twython import Twython

from twitter_watcher.server import api
from twitter_watcher.db.models import Listener
from twitter_watcher.clients import TwitterClient, TwitterWatcherStream

APP_KEY = api.config['APP_TWIITER_ID']
APP_TWIITER_ID=api.config['APP_TWIITER_ID']
APP_SECRET = api.config['APP_TWIITER_SECRET']
OAUTH_KEY = api.config['TOKEN_TWIITER_ID']
OAUTH_TOKEN = api.config['TOKEN_TWIITER_SECRET']


log = logging.getLogger(__name__)


class Twitter(Command):
    """ Command that start twitter stream listener """

    def run(self):
        log.info('Starting listenning')
        twitter_client = Twython(APP_KEY, APP_SECRET, OAUTH_KEY, OAUTH_TOKEN)
        stream_client = TwitterWatcherStream(APP_KEY, APP_SECRET,
                                             OAUTH_KEY, OAUTH_TOKEN)
        listeners = Listener.objects

        log.info("We have %s listeners", len(listeners))

        client = TwitterClient(stream_client=stream_client,
                               twitter_client=twitter_client,
                               listeners=listeners)

        client.start()
