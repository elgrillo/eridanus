# from google.appengine.api import users
from flask import Flask, render_template
from flask_wtf import CSRFProtect
from flask_wtf.csrf import CSRFError
from apps.eridanus.controllers import AdminController, CrunchesController, \
    HomeController, WeightController
from app.activities.running.blueprint import running_activities
from app.activities.pushups.blueprint import pushup_activities
from config import Configuration


app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['DEBUG'] = True
# app.config['WTF_CSRF_SECRET_KEY'] = False
app.config['SECRET_KEY'] = Configuration.SECRET_KEY
app.register_blueprint(pushup_activities, url_prefix='/pushups/activities')
app.register_blueprint(running_activities, url_prefix="/running/activities")


# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
@app.route('/home')
@csrf.exempt
def home():
    controller = HomeController()
    return controller.index()


@app.route('/admin')
def admin():
    controller = AdminController()
    return controller.index()


@app.route('/admin/export')
def admin_export():
    controller = AdminController()
    return controller.export()


@app.route('/admin/import')
def admin_import():
    controller = AdminController()
    return controller.import_data()

# RUNNING
# @app.route('/activities/runnings')
# def runnings():
#     controller = RunController()
#     return controller.list()


# @app.route('/activities/runnings/create', methods=['GET'])
# def runnings_create():
#     controler = RunController()
#     return controler.new()


# @app.route('/activities/runnings/create', methods=['POST'])
# @csrf.exempt
# def runnings_save():
#     controller = RunController()
#     return controller.save()

# PUSH-UPS
# @app.route('/activities/pushups', methods=['GET'])
# def pushups():
#     controller = PushUpsController()
#     return controller.list()

# @app.route('/activities/pushups/create', methods=['GET'])
# def pushups_create():
#     controller = PushUpsController()
#     if request.method == 'GET':
#         return controller.get_create_form()

# @app.route('/activities/pushups/create', methods=['POST'])
# @csrf.exempt
# def pushups_save():
#     controller = PushUpsController()
#     return controller.add_pushup()

# CRUNCHES
@app.route('/activities/crunches', methods=['GET'])
def crunches():
    controller = CrunchesController()
    return controller.list()


@app.route('/activities/crunches/create', methods=['GET'])
def crunches_create():
    controller = CrunchesController()
    return controller.create()


@app.route('/activities/crunches/create', methods=['POST'])
@csrf.exempt
def crunches_process_create_form():
    controller = CrunchesController()
    return controller.process_create_form()


# WEIGHING ROUTES
@app.route('/weighings')
def weighings():
    controller = WeightController()
    return controller.list()


@app.route('/weighings/create', methods=['GET'])
def weighings_create():
    controller = WeightController()
    return controller.create()


@app.route('/weighings/create', methods=['POST'])
@csrf.exempt
def weighings_save():
    controller = WeightController()
    return controller.save()


# ERROR HANDLING
@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404


@app.errorhandler(401)
def unauthorized(e):
    """Return not authorized."""
    return 'You''re not authorized to use this website', 401
