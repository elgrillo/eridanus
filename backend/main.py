from google.appengine.api import users
from flask import Flask, redirect, render_template, session, url_for
from flask_wtf import CSRFProtect
from flask_wtf.csrf import CSRFError

from config import Configuration
from eridanus.admin.blueprint import admin
from eridanus.activities.crunches.blueprint import crunches
from eridanus.activities.running.blueprint import running_activities
from eridanus.activities.pushups.blueprint import pushup_activities
from eridanus.dashboard.blueprint import dashboard
from eridanus.weighing.blueprint import weighings

from eridanus.api.v1 import api


app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['DEBUG'] = True
# app.config['WTF_CSRF_SECRET_KEY'] = False
app.config['SECRET_KEY'] = Configuration.SECRET_KEY
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(crunches, url_prefix='/activities/crunches')
app.register_blueprint(pushup_activities, url_prefix='/activities/pushups')
app.register_blueprint(running_activities, url_prefix="/activities/running")
app.register_blueprint(weighings, url_prefix='/weighings')
app.register_blueprint(dashboard, url_prefix='/dashboard')
app.register_blueprint(api, url_prefix='/api/v1')


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
