from .constants import ERIDANUS_DATE_FORMAT, ERIDANUS_TIME_FORMAT
from datetime import datetime


def format_date(date_value):
    return date_value.strftime(ERIDANUS_DATE_FORMAT)


def format_time(time_value):
    return time_value.strftime(ERIDANUS_TIME_FORMAT)


def to_date(date_value, format):
    return datetime.strptime(date_value, format).date()


def to_time(time_value, format):
    return datetime.strptime(time_value, format).time()


def to_datetime(datetime_value, format):
    return datetime.strptime(datetime_value, format)
