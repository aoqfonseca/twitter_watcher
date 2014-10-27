# -*- coding: utf-8 -*-

from mongoengine import Document
from mongoengine.fields import ListField, StringField, DateTimeField

from twitter_watcher.observers import ObserverTwitter


class Listener(Document, ObserverTwitter):
    usernames = ListField(StringField())
    hashtags = ListField(StringField())
    callback = StringField()
    type = StringField()
    start_date = DateTimeField(db_field='startDate')
    end_date = DateTimeField(db_field='endDate')

    def to_json(self):
        return {
            u'id': str(self.id),
            u'usernames': self.usernames,
            u'hashtags': self.hashtags,
            u'startDate': self.start_date,
            u'endDate': self.end_date
        }

    @property
    def url(self):
        return self.callback
