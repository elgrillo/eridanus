from wtforms import IntegerField
from ..forms import ActivityForm


class PushupForm(ActivityForm):
    count = IntegerField()