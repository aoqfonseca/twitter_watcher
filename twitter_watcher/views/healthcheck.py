# -*- coding: utf-8 -*-
from flask.views import MethodView


class HealthCheck(MethodView):

    def get(self):
        return "WORKING", 200
