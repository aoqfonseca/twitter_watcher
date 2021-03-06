# -*- coding: utf-8 -*-
import json
import arrow
import logging

from flask import Response, Blueprint, request, jsonify
from flask.views import MethodView

from mongoengine.errors import ValidationError

from twitter_watcher.schema import valid_json_listener
from twitter_watcher.db.models import Listener


listeners_view = Blueprint('listeners_view', __name__)

log = logging.getLogger(__name__)


class ListView(MethodView):

    def get(self):
        listeners = Listener.objects
        listeners = [listener.to_json() for listener in listeners]
        return jsonify(listeners=listeners)


class DetailView(MethodView):

    def get(self, id):
        try:
            listener = Listener.objects.get(id=id)
            return jsonify(listener.to_json())
        except Listener.DoesNotExist:
            return Response('Not Exist', status=404)
        except ValidationError:
            return Response('Bad Request', 400)

    def post(self):
        if request.headers['content-type'] != 'application/json':
            return Response(status=406)

        try:
            data = json.loads(request.data)

            if valid_json_listener(data) is not True:
                log.error('json invalid')
                return Response(status=400)

            start_date = data.get('startDate')
            start_date = arrow.get(start_date).datetime

            end_date = data.get('endDate')
            end_date = arrow.get(end_date).datetime

        except ValueError, e:
            log.error('ValueError %s ', e)
            return Response(status=400)
        except arrow.parser.ParserError:
            log.error('Error parsing date')
            return Response(status=400)

        listener = Listener(usernames=data['usernames'],
                            hashtags=data['hashtags'],
                            callback=data['callback'],
                            type=data['type'],
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
            listener.callback = data['callback']
            listener.type = data['type']
            listener.start_date = start_date
            listener.end_date = end_date

            listener.save()

        except ValueError:
            return Response(status=400)
        except arrow.parser.ParserError:
            return Response(status=400)

        return Response(status=200)

    def delete(self, id):
        if request.headers['content-type'] != 'application/json':
            return Response(status=406)

        Listener.objects.get(id=id).delete()
        return Response(status=200)


listeners_view.add_url_rule('/listeners',
                            view_func=DetailView.as_view('create'),
                            methods=['POST'])

listeners_view.add_url_rule('/listeners',
                            view_func=ListView.as_view('index'),
                            methods=['GET'])

listeners_view.add_url_rule('/listener/<id>',
                            view_func=DetailView.as_view('listener'),
                            methods=['GET', 'PUT', 'DELETE'])
