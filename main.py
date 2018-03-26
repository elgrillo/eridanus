from google.appengine.api import users
from flask import Flask, redirect, render_template, session, url_for
from flask_wtf import CSRFProtect
from flask_wtf.csrf import CSRFError
from controllers import AdminController
from app.activities.crunches.blueprint import crunches
from app.activities.running.blueprint import running_activities
from app.activities.pushups.blueprint import pushup_activities
from app.dashboard.blueprint import dashboard
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
app.register_blueprint(dashboard, url_prefix='/dashboard')


# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

# TODO: use flask-login decorators to restrict access to views
@app.before_request
def check_authentication():
    if 'nickname' not in session:
        user = users.get_current_user()
        if user:
            session['nickname'] = user.nickname()
            _auth_domain = None
            session['logout_url'] = users.create_logout_url('/', _auth_domain)


@app.route('/')
@app.route('/home')
@csrf.exempt
def home():
    return redirect(url_for('dashboard.index'), 302)


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
