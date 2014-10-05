# -*- coding: utf-8 -*-
import os
import logging

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from twitter_watcher.views import register_blueprints

api = Flask(__name__)
api.debug = os.environ.get('API_DEBUG', 0) in ('true', 'True', '1')

api.config['MONGODB_SETTINGS'] = {
    'DB': os.environ.get('MONGODB_URL', 'twitter_watcher')
}

api.config['SECRET_KEY'] = 'KeepThisS3cr3t3'

db = MongoEngine()

db.init_app(api)
register_blueprints(api)


log = logging.getLogger(__name__)

@api.route('/test',  methods=['GET', 'POST'])
def test():
	log.info("Chegou mensagem")
	return "ok"