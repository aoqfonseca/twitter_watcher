# -*- coding: utf-8 -*-
import logging

from flask.ext.script import Command
from twython import Twython

from twitter_watcher.db.models import Listener
from twitter_watcher.clients import TwitterClient, TwitterWatcherStream

APP_KEY = 'zBO5D1AEtirDc2vxGYPD8BWxf'
APP_SECRET = '8YD072ZmiePSNXGpywTSgFYfMRhgQe075v99nuSg8GzQMw5Cw8'
OAUTH_KEY = '12278792-UsFcoPJiinLDott7TTChdSfVwcbOf7ZWqjNjNkp5A'
OAUTH_TOKEN = '4ci9LIIaN7prrJszpGf66eWKxhiwqeMP9ta0tOZAHx8lC'


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
