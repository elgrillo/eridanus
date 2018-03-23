from datetime import datetime
from flask import Blueprint, flash, redirect, \
    render_template, request, session, url_for
from ..forms import PushupForm
from ..services import PushupsService


pushup_activities = Blueprint(
    'pushup_activities',
    __name__,
    template_folder='templates')
service = PushupsService()


def _validate_form(form):
    ''' TODO: not yet implemented '''
    return True


@pushup_activities.route("/")
@pushup_activities.route("/list/")
def index():
    username = session['nickname']
    if username:
        items = service.fetch_all(username)
        return render_template(
            'activities/pushups/index.html', viewmodel={'items': items})
    else:
        # TODO: redirect to the authentication page
        pass


@pushup_activities.route("/create/", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        form = PushupForm()
        if _validate_form(form):
            service.create({
                'activity_date': form.activity_date.data,
                'activity_time': datetime.strptime(
                    form.activity_time.data,
                    '%H:%M'
                    ).time(),
                'calories': form.calories.data,
                'count': form.count.data,
                'duration': form.duration.data,
                'notes': form.notes.data,
                'user_nickname': session['nickname']
                })
            flash('Push-ups activity "%s" created successfully.', 'success')
            return redirect(url_for('pushup_activities.index'), 302)
    else:
        form = PushupForm()
        return render_template('activities/pushups/create.html', form=form)


@pushup_activities.route('/<activity_id>/', methods=['GET', 'POST'])
def view(activity_id):
    ''' REVIEW: TEST: TODO: '''
    activity = service.fetch(activity_id)
    if activity:
        return render_template('activities/pushups/view.html', activity)
    else:
        return redirect(url_for('app.page_not_found', 302))


@pushup_activities.route("/<activity_id>/edit", methods=['GET', 'POST'])
def edit(activity_id):
    ''' REVIEW: review this method as is not fully implemented,
    is just a stub
    '''
    if request.method == 'POST':
        form = PushupForm()
        if _validate_form(form):
            service.update({
                'activity_id': activity_id,
                'activity_date': form.activity_date.data,
                'activity_time': datetime.strptime(
                    form.activity_time.data,
                    '%H:%M'
                    ).time(),
                'calories': form.calories.data,
                'count': form.count.data,
                'duration': form.duration.data,
                'notes': form.notes.data,
                'user_nickname': session['nickname']
            })
            flash('Push-ups activity "%s" saved successfully.', 'success')
            return redirect(url_for('pushup_activities.index'), 302)
        else:
            pass
    else:
        activity = service.fetch(activity_id)
        if activity:
            form = PushupForm()
            form.activity_date = activity['activity_date']
            return render_template(
                'activities/pushups/edit.html',
                form=form)
        else:
            pass  # TODO: if None then return 404 .first_or_404()


@pushup_activities.route("/<activity_id>/delete/", methods=['POST'])
def delete(activity_id):
    ''' REVIEW: review this method as is not fully implemented,
    is just a stub
    '''
    service.delete(activity_id)
    flash('Push-ups activity "%s" saved successfully.', 'success')
    return redirect(url_for('pushup_activities.index'), 302)


@pushup_activities.errorhandler(404)
def page_not_found(e):
    return 'Sorry, nothing at this URL.', 404
    # TODO: return render_template('pages/404.html')
