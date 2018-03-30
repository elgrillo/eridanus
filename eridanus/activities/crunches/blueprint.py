from datetime import datetime
from flask import Blueprint, flash, \
    redirect, render_template, request, session, url_for
from ..forms import CrunchesForm
from ..services import CrunchesService

crunches = Blueprint('crunches', __name__, template_folder='templates')
service = CrunchesService()


def _validate_form(form):
    return True


@crunches.route('/', methods=['GET'])
@crunches.route('/list/', methods=['GET'])
def index():
    username = session['nickname']
    if username:
        items = service.fetch_all(username)
        return render_template(
            'activities/crunches/index.html',
            viewmodel={'items': items})
    else:
        pass


@crunches.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        form = CrunchesForm()
        if _validate_form(form):
            service.create({
                'activity_date': form.activity_date.data,
                'activity_time': (
                        datetime
                        .strptime(form.activity_time.data, '%H:%M')
                        .time()
                    ),
                'duration': form.duration.data,
                'calories': form.calories.data,
                'count': form.count.data,
                'notes': form.notes.data,
                'user_nickname': session['nickname']
            })
            flash('Activity "%s" created successfully.', 'success')
            return redirect(url_for('crunches.index'), 302)
        else:
            pass
    else:
        form = CrunchesForm()
        return render_template('activities/crunches/create.html', form=form)
