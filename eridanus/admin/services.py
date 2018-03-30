
from StringIO import StringIO

import csv
import eridanus.repository as repository


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
    pass
