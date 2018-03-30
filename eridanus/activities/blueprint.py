from flask import Blueprint, render_template


activities = Blueprint('activities', __name__, template_folder='templates')


@activities.route('/')
def index():
    return render_template('/index.html', vm={})
