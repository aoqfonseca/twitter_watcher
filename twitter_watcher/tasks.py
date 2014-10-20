# -*- coding: utf-8 -*-
from functools import partial
from twitter_watcher.db.models import Listener


def call_listener(msg, listener):
    """ This functio will process each message and listener"""
    listener.on_message(msg)


def receive_msg(msg):
    func = partial(call_listener, msg)
    listeners = Listener.objects
    map(func, listeners)
