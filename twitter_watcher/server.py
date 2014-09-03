# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from twitter_watcher.views import HealthCheck, ListenerView

api = Flask(__name__)
api.debug = os.environ.get('API_DEBUG', 0) in ('true', 'True', '1')

api.config['MONGODB_SETTINGS'] = {
    'DB': os.environ.get('MONGODB_URL', 'twitter_watcher')
}

api.config['SECRET_KEY'] = 'KeepThisS3cr3t3'

db = MongoEngine(api)

api.add_url_rule('/healthcheck', view_func=HealthCheck.as_view('healthcheck'))
api.add_url_rule('/listeners',
                 view_func=ListenerView.as_view('listeners'),
                 methods=['POST'])

api.add_url_rule('/listener/<id>',
                 view_func=ListenerView.as_view('listener'),
                 methods=['GET', 'PUT', 'DELETE'])
