from flask import jsonify
from flask import session
from flask_restful import fields
from flask_restful import Resource
from eridanus.dashboard.services import DashboardService


class Dashboard(Resource):
    ''' Dashboard resource '''
    def get(self):
        username = session['nickname']
        if username:
            stats = DashboardService().home_stats(username)
            return jsonify(stats)

    def post(self):
        pass

