# -*- coding: utf-8 -*-

from mongoengine import Document
from mongoengine.fields import ListField, StringField, DateTimeField


class Listener(Document):
	usernames = ListField(StringField())
	hashtags = ListField(StringField())
	start_date = DateTimeField()
	end_date = DateTimeField()