# -*- coding: utf-8 -*-

from flask import Response, request
from flask.views import MethodView

from twitter_watcher.schema import valid_json_listener


class Listener(MethodView):

    def post(self):
        if request.headers['content-type'] != 'application/json':
            return Response(status=400)

        json = request.data

        if valid_json_listener(json) is not True:
            return Response(status=405)

        return Response(status=201)
