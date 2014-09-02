# -*- coding: utf-8 -*-
import json
import arrow

from flask import Response, request
from flask.views import MethodView

from twitter_watcher.schema import valid_json_listener


class Listener(MethodView):

    def post(self):
        if request.headers['content-type'] != 'application/json':
            return Response(status=406)

        try:
            data = json.loads(request.data)

            if valid_json_listener(data) is not True:
                return Response(status=400)

            start_date = data.get('startDate')
            start_date = arrow.get(start_date)

        except ValueError:
            return Response(status=400)
        except arrow.parser.ParserError:
            return Response(status=400)

        return Response(status=201)
