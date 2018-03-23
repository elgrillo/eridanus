# from google.appengine.api import users
from flask import Flask, render_template
from flask_wtf import CSRFProtect
from flask_wtf.csrf import CSRFError
from controllers import AdminController, HomeController
from app.activities.crunches.blueprint import crunches
from app.activities.running.blueprint import running_activities
from app.activities.pushups.blueprint import pushup_activities
from app.weighing.blueprint import weighings
from config import Configuration


app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['DEBUG'] = True
# app.config['WTF_CSRF_SECRET_KEY'] = False
app.config['SECRET_KEY'] = Configuration.SECRET_KEY
app.register_blueprint(crunches, url_prefix='/activities/crunches')
app.register_blueprint(pushup_activities, url_prefix='/activities/pushups')
app.register_blueprint(running_activities, url_prefix="/activities/running")
app.register_blueprint(weighings, url_prefix='/weighings')


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
