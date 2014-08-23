# -*- coding: utf-8 -*-
import os

from flask import Flask

api = Flask(__name__)
api.debug = os.environ.get('API_DEBUG', 0) in ('true', 'True', '1')


@api.route('/healthcheck')
def healthcheck():
    return "WORKING", 200
