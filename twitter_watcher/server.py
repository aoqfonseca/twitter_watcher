# -*- coding: utf-8 -*-
import os

from flask import Flask
from twitter_watcher.views import HealthCheck

api = Flask(__name__)
api.debug = os.environ.get('API_DEBUG', 0) in ('true', 'True', '1')

api.add_url_rule('/healthcheck', view_func=HealthCheck.as_view('healthcheck'))
