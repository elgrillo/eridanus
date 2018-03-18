from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField
from wtforms import TextField, TextAreaField
# from wtforms_components import TimeField
from wtforms.validators import DataRequired
from datetime import datetime


class ActivityForm(FlaskForm):
    activity_date = DateField(
        label='activity_date',
        default=datetime.now(),
        validators=[DataRequired])
    activity_time = TextField(
        label='activity_time',
        default=datetime.now().time().strftime('%I:%M %p'),
        validators=[DataRequired])
    duration = IntegerField()
    calories = IntegerField()
    notes = TextAreaField()
