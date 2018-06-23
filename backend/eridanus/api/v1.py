from flask import Blueprint
from flask_restful import Api
from .resources.dashboard import Dashboard
from .resources.activities import Running


api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)
api.add_resource(Dashboard, '/stats/')
api.add_resource(Running, '/activities/running/')

# @api.route('/stats/', methods=['GET'])
# def get_stats():
#     username = session['nickname']
#     if username:
#         stats = DashboardService().home_stats(username)
#         return jsonify(stats)
#     else:
#         return jsonify({'error': 'Access denied'})


# @api.route('/activities/running/', methods=['GET'])
# def get_all_running_activities():
#     username = session['nickname']
#     if username:
#         data = RunningService().fetch_all(username)
#         return jsonify(data)
