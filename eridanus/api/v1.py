from flask import Blueprint
from flask import jsonify
from flask import session
from eridanus.dashboard.services import DashboardService
from eridanus.activities.services import RunningService

api = Blueprint('api', __name__)


@api.route('/stats/', methods=['GET'])
def get_stats():
    username = session['nickname']
    if username:
        stats = DashboardService().home_stats(username)
        return jsonify(stats)
    else:
        return jsonify({'error': 'Access denied'})


@api.route('/activities/running/', methods=['GET'])
def get_all_running_activities():
    username = session['nickname']
    if username:
        data = RunningService().fetch_all(username)
        return jsonify(data)
