from google.appengine.api import app_identity
from flask import render_template, \
    make_response
from datetime import datetime
from zipfile import ZipFile
from StringIO import StringIO
from repository import RunRepository, WeightRepository

import cloudstorage as gcs
import csv
import os


def _get_default_bucket():
    bucket_name = os.environ.get(
        'BUCKET_NAME',
        app_identity.get_default_gcs_bucket_name())
    return bucket_name


def _read_file(filename):
    gcs_file = gcs.open(filename)
    contents = gcs_file.read()
    gcs_file.close()
    return contents


def import_from_csv(folder):
    default_bucket = _get_default_bucket()
    if default_bucket:
        import_folder = default_bucket + '/import/' + folder
        _import_run_csv(import_folder)
        _import_weight_csv(import_folder)


def _import_run_csv(import_folder):
    filename = import_folder + '/run.csv'
    content = _read_file(filename)
    stream = StringIO(content)
    csvReader = csv.DictReader(stream, dialect='excel')
    for row in csvReader:
        repo = RunRepository()
        repo.create({
            'user_nickname': row['usernickname'],
            'activity_date': row['activity_date'],
            'activity_time': row['activity_time'],
            'duration': row['duration'],
            'distance': row['distance'],
            'speed': row['speed'],
            'calories': row['calories'],
            'notes': row['notes'],
            'creation_datetime': row['creation_datetime']
        })


def _import_weight_csv(import_folder):
    filename = import_folder + '/weight.csv'
    content = _read_file(filename)
    stream = StringIO(content)
    csvReader = csv.DictReader(stream, dialect='excel')
    for row in csvReader:
        repo = WeightRepository()
        repo.create({
            'user_nickname': row['usernickname'],
            'weight': row['weight'],
            'weighing_date': row['creation_datetime'],
            'creation_datetime': row['creation_datetime']
        })


def export_csv():
    run_csv = _build_run_csv()
    weight_csv = _build_weight_csv()
    in_memory = StringIO()
    zip = ZipFile(in_memory, "a")
    zip.writestr("run.csv", run_csv)
    zip.writestr("weight.csv", weight_csv)
    # fix for Linux zip files read in Windows
    for file in zip.filelist:
        file.create_system = 0
    zip.close()
    in_memory.seek(0)
    response = make_response(in_memory.read())
    response.headers["Content-Disposition"] = "attachment; filename=eridanus_data.zip"
    response.headers['Cache-Control'] = 'no-cache'
    response.headers['Content-Type'] = 'application/zip'
    # in_memory.seek(0)    
    # response.write(in_memory.read()) #?
    return response


def _build_run_csv():
    items = _fetch_all_run()
    stream = StringIO()
    fieldnames = [
        'usernickname', 'activity_date', 'activity_time',
        'duration', 'distance', 'speed',
        'calories', 'notes', 'creation_datetime']
    csvwriter = csv.DictWriter(stream, fieldnames=fieldnames, dialect='excel')
    csvwriter.writeheader()
    for item in items:
        csvwriter.writerow({
            'usernickname': item.usernickname, 
            'activity_date': _get_activity_date(item),
            'activity_time': _get_activity_time(item),
            'duration': _get_duration(item),
            'distance': item.distance,
            'speed': item.speed,
            'calories': item.calories,
            'notes': item.notes,
            'creation_datetime': item.creation_datetime
            })
    return stream.getvalue()


def _build_weight_csv():
    items = _fetch_all_weights()
    stream = StringIO()
    csvwriter = csv.writer(stream, dialect='excel')
    fieldnames = ['usernickname', 'weight', 'creation_datetime']
    csvwriter = csv.DictWriter(stream, fieldnames=fieldnames, dialect='excel')
    csvwriter.writeheader()
    for item in items:
        csvwriter.writerow({
            'usernickname': item.usernickname, 
            'weight': item.weight,
            'creation_datetime': item.creation_datetime
            })
    return stream.getvalue()


def _build_csv(items):
    pass


def _fetch_all_run():
    repo = RunRepository()
    return repo.fetch_all()


def _fetch_all_weights():
    repo = WeightRepository()
    return repo.fetch_all()


def _get_activity_date(model):
    if model.activity_date:
        return model.activity_date
    else:
        return model.date


def _get_activity_time(model):
    if model.activity_time:
        return model.activity_time
    else:
        return datetime.strptime(u'20:30', '%H:%M').time()


def _get_duration(model):
    if model.duration:
        return model.duration
    else:
        return model.time


def import_data():
    pass


def index():
    return render_template('admin/home.html')