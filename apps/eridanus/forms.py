from flask_wtf import FlaskForm
from wtforms import IntegerField, DecimalField, \
    DateField, TextField, TextAreaField 
# from wtforms_components import TimeField
from wtforms.validators import DataRequired
from datetime import datetime


class WeightForm(FlaskForm):
    weighing_date = DateField(
        label='weighing_date', 
        default=datetime.now(), 
        validators=[DataRequired])
    weight = DecimalField(label='weight', validators=[DataRequired])


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


# class RunForm(ActivityForm):
#     time = IntegerField(validators=[DataRequired])
#     distance = DecimalField(validators=[DataRequired])


# class PushUpForm(ActivityForm):
#     count = IntegerField()

    
class CrunchActivityForm(ActivityForm):
    count = IntegerField()