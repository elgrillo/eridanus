from flask import Blueprint, flash, render_template, \
    redirect, session, request, url_for
from datetime import datetime
from ..forms import RunningForm
from ..services import RunningService

service = RunningService()

running_activities = Blueprint(
    'running_activities',
    __name__,
    template_folder='templates')


def _validate_form(form):
    ''' TODO: not yet implemented '''
    return True


@running_activities.route("/")
@running_activities.route("/list/")
def index():
    ''' create the viewmodel and return the view '''
    username = session['nickname']
    if username:
        items = service.fetch_all(username)
        return render_template('activities/running/index.html', vm=items)


@running_activities.route("/create/", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        form = RunningForm()
        if _validate_form(form):
            distance = float(form.distance.data)
            duration = form.duration.data
            speed = distance / (float(duration)/60.0)

            service.create({
                    'activity_date': form.activity_date.data,
                    'activity_time': datetime.strptime(
                        form.activity_time.data,
                        '%H:%M'
                        ).time(),
                    'distance': distance,
                    'duration': duration,
                    'calories': form.calories.data,
                    'notes': form.notes.data,
                    'speed': speed,
                    'user_nickname': session['nickname']
                })
            flash('Activity "%s" created successfully.', 'success')
            return redirect(url_for('running_activities.index'), 302)
    else:
        form = RunningForm()
        return render_template('activities/running/create.html', form=form)


# @running_activities.route("/edit/<activity>/", methods = ["GET"])
# def read():
#     form = RunningForm()
#     return render_template('edit.html', form=form)


@running_activities.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html')
