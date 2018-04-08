from flask import Blueprint, flash, render_template, \
    redirect, request, session, url_for
from .forms import WeightForm
from .services import WeighingService


weighings = Blueprint("weighings", __name__, template_folder='templates')
service = WeighingService()


def _validate_form(form):
    return True


@weighings.route("/")
@weighings.route("/list/")
def index():
    username = session['nickname']
    if username:
        items = service.fetch_all(username)
        return render_template('weighings/index.html', vm=items)
    else:
        # TODO: redirect to login page
        pass


@weighings.route("/create/", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        form = WeightForm()
        if (_validate_form(form)):
            service.create({
                'user_nickname': session['nickname'],
                'weight': float(form.weight.data),
                'weighing_date': form.weighing_date.data
            })
            flash('Weighing record "%s" created successfully.', 'success')
            return redirect(url_for('weighings.index'), 302)
    else:
        form = WeightForm()
        return render_template('weighings/create.html', form=form)

