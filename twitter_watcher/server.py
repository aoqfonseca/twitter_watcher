# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask.ext.mongoengine import MongoEngine

from celery import Celery

from twitter_watcher.views import register_blueprints

api = Flask(__name__)
api.config.from_object('twitter_watcher.config.Config')

db = MongoEngine()

db.init_app(api)
register_blueprints(api)

app_celery = Celery()
app_celery.conf.update(BROKER_URL=api.config['BROKER_URL'])
