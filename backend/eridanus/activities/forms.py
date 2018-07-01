from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, DecimalField, \
    TextAreaField, StringField
# from wtforms_components import TimeField
from wtforms.validators import DataRequired
from datetime import datetime


class ActivityForm(FlaskForm):
    current_datetime = datetime.now()
    activity_date = DateField(
        label='activity_date',
        default=current_datetime,
        validators=[DataRequired])
    # https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/time 
    # https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
    activity_time = StringField(
        label='activity_time',
        default=current_datetime.time().strftime('%H:%M'),
        validators=[DataRequired])
    duration = IntegerField()
    calories = IntegerField()
    notes = TextAreaField()


class CrunchesForm(ActivityForm):
    count = IntegerField()


class PushupForm(ActivityForm):
    count = IntegerField()


class RunningForm(ActivityForm):
    # time = IntegerField(validators=[DataRequired])
    distance = DecimalField(validators=[DataRequired])


class JumpRopeForm(ActivityForm):
    count = IntegerField()
