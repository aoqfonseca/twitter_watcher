# -*- coding: utf-8 -*-

from mongoengine import Document
from mongoengine.fields import ListField, StringField, DateTimeField

from twitter_watcher.observers import ObserverTwitter


class Listener(Document, ObserverTwitter):
    usernames = ListField(StringField())
    hashtags = ListField(StringField())
    callback = StringField()
    start_date = DateTimeField(db_field='startDate')
    end_date = DateTimeField(db_field='endDate')
