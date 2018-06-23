from flask import jsonify, session
from flask_restful import Resource
from eridanus.activities.services import RunningService


class Running(Resource):

    def get(self):
        username = session['nickname']
        if username:
            data = RunningService().fetch_all(username)
            return jsonify(data)

    def post(self):
        pass
