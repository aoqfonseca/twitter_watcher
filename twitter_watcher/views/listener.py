# -*- coding: utf-8 -*-
import json
import arrow

from flask import Response, request
from flask.views import MethodView

from twitter_watcher.schema import valid_json_listener
from twitter_watcher.db.models import Listener


class ListenerView(MethodView):

    def get(self, id):
        return "oi", 200

    def post(self):
        if request.headers['content-type'] != 'application/json':
            return Response(status=406)

        try:
            data = json.loads(request.data)

            if valid_json_listener(data) is not True:
                return Response(status=400)

            start_date = data.get('startDate')
            start_date = arrow.get(start_date).datetime

            end_date = data.get('endDate')
            end_date = arrow.get(end_date).datetime

        except ValueError:
            return Response(status=400)
        except arrow.parser.ParserError:
            return Response(status=400)

        listener = Listener(usernames=data['usernames'],
                            hashtags=data['hashtags'],
                            callback=data['callback'],
                            start_date=start_date,
                            end_date=end_date)
        listener.save()

        return Response(status=201)

    def put(self, id):
        if request.headers['content-type'] != 'application/json':
            return Response(status=406)

        try:
            data = json.loads(request.data)

            if valid_json_listener(data) is not True:
                return Response(status=400)

            start_date = data.get('startDate')
            start_date = arrow.get(start_date).datetime

            end_date = data.get('endDate')
            end_date = arrow.get(end_date).datetime

            listener = Listener.objects.get(id=id)
            listener.usernames = data['usernames']
            listener.hashtags = data['hashtags']
            listener.start_date = start_date
            listener.end_date = end_date

            listener.save()

        except ValueError:
            return Response(status=400)
        except arrow.parser.ParserError:
            return Response(status=400)

        return Response(status=200)
