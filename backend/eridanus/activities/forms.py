from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, DecimalField, \
    TextField, TextAreaField
# from wtforms_components import TimeField
from wtforms.validators import DataRequired
from datetime import datetime


class ActivityForm(FlaskForm):
    current_datetime = datetime.now() 
    activity_date = DateField(
        label='activity_date',
        default=current_datetime,
        validators=[DataRequired])
    activity_time = TextField(
        label='activity_time',
        default=current_datetime.time().strftime('%I:%M %p'),
        validators=[DataRequired])
    duration = IntegerField()
    calories = IntegerField()
    notes = TextAreaField()


class CrunchesForm(ActivityForm):
    count = IntegerField()


class PushupForm(ActivityForm):
    count = IntegerField()


class RunningForm(ActivityForm):
    time = IntegerField(validators=[DataRequired])
    distance = DecimalField(validators=[DataRequired])
