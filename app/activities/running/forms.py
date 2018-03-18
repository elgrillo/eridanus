from wtforms import IntegerField, DecimalField
from wtforms.validators import DataRequired
from ..forms import ActivityForm


class RunForm(ActivityForm):
    time = IntegerField(validators=[DataRequired])
    distance = DecimalField(validators=[DataRequired])
