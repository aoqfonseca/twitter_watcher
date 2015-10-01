# -*- coding: utf-8 -*-
from functools import partial
from twitter_watcher.db.models import Listener
from twitter_watcher.server import app_celery


def call_listener(msg, listener):
    listener.on_message(msg)

@app_celery.task
def receive_msg(msg):
    func = partial(call_listener, msg)
    listeners = Listener.objects
    map(func, listeners)
