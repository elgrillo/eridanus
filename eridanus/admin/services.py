from ..utils import to_date, to_time, to_datetime
from google.appengine.api import app_identity
from StringIO import StringIO

import csv
import cloudstorage as gcs
import os
import eridanus.repository as repository

IMPORT_DATE_FORMAT = '%Y-%m-%d'
IMPORT_TIME_FORMAT = '%H:%M:%S'
IMPORT_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S.%f'


class ExportDataService(object):

    def get_run_data(self, username, format):
        repo = repository.RunRepository()
        items = repo.fetch_all(username)
        stream = StringIO()
        fieldnames = ['usernickname', 'activity_date', 'activity_time',
                      'time', 'distance', 'speed', 'calories', 
                      'notes', 'creation_datetime']
        csvwriter = csv.DictWriter(
                        stream,
                        fieldnames=fieldnames,
                        dialect='excel')
        csvwriter.writeheader()
        for item in items:
            csvwriter.writerow({
                'usernickname': item.usernickname, 
                'activity_date': item.activity_date,
                'activity_time': item.activity_item,
                'duration': item.duration,
                'distance': item.distance,
                'speed': item.speed,
                'calories': item.calories,
                'notes': item.notes,
                'creation_datetime': item.creation_datetime
                })
        return stream.getvalue()

    def get_weight_data(self, username, format):
        repo = repository.WeightRepository()
        items = repo.fetch_all(username)
        stream = StringIO()
        csvwriter = csv.writer(stream, dialect='excel')
        fieldnames = ['usernickname', 'weight', 'creation_datetime']
        csvwriter = csv.DictWriter(
            stream,
            fieldnames=fieldnames,
            dialect='excel')
        csvwriter.writeheader()
        for item in items:
            csvwriter.writerow({
                'usernickname': item.usernickname,
                'weight': item.weight,
                'creation_datetime': item.creation_datetime
                })
        return stream.getvalue()


class ImportDataServices(object):

    def import_from_csv(self, folder, username):
        audit = {}
        default_bucket = self._get_default_bucket()
        audit['default_bucket'] = default_bucket
        if default_bucket:
            import_folder = "/" + default_bucket + '/import/' + folder
            # self._import_run_csv(import_folder)
            self._import_weight_csv(import_folder)

    def _get_default_bucket(self):
        bucket_name = os.environ.get(
            'BUCKET_NAME',
            app_identity.get_default_gcs_bucket_name())
        return bucket_name

    def _read_file(self, filename):
        gcs_file = gcs.open(filename)
        contents = gcs_file.read()
        gcs_file.close()
        return contents

    def _import_run_csv(self, import_folder):
        audit = {}
        filename = import_folder + '/run.csv'
        content = self._read_file(filename)
        stream = StringIO(content)
        csvReader = csv.DictReader(stream, dialect='excel')
        for row in csvReader:
            repo = repository.RunRepository()
            duration = int(row['duration'])
            distance = float(row['distance'])
            speed = None
            if row['speed']:
                speed = float(row['speed'])
            else:
                speed = distance / (duration / 60.0)
            repo.create({
                'user_nickname': row['usernickname'],
                'activity_date': to_date(
                    row['activity_date'], IMPORT_DATE_FORMAT),
                'activity_time': to_time(
                    row['activity_time'], IMPORT_TIME_FORMAT),
                'duration': duration,
                'distance': distance,
                'speed': speed,
                'calories': int(row['calories']),
                'notes': row['notes'],
                'creation_datetime': to_datetime(
                    row['creation_datetime'], IMPORT_DATETIME_FORMAT)
            })
        audit['filename'] = filename
        return audit

    def _import_weight_csv(self, import_folder):
        filename = import_folder + '/weight.csv'
        content = self._read_file(filename)
        stream = StringIO(content)
        csvReader = csv.DictReader(stream, dialect='excel')
        for row in csvReader:
            repo = repository.WeightRepository()
            repo.create({
                'user_nickname': row['usernickname'],
                'weight': float(row['weight']),
                'weighing_date': to_date(
                    row['creation_datetime'], IMPORT_DATETIME_FORMAT),
                'creation_datetime': to_datetime(
                    row['creation_datetime'], IMPORT_DATETIME_FORMAT)
            })
