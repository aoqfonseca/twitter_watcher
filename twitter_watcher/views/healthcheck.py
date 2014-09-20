# -*- coding: utf-8 -*-
from flask import Blueprint
from flask.views import MethodView


healthcheck = Blueprint('healthchek', __name__)

class HealthCheck(MethodView):

    def get(self):
        return "WORKING", 200


healthcheck.add_url_rule('/healthcheck',
						 view_func=HealthCheck.as_view('healthcheck'))
