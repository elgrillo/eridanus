from .constants import ERIDANUS_DATE_FORMAT, ERIDANUS_TIME_FORMAT


def format_date(date_value):
    return date_value.strftime(ERIDANUS_DATE_FORMAT)


def format_time(time_value):
    return time_value.strftime(ERIDANUS_TIME_FORMAT)