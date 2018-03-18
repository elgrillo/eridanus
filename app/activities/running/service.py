from app.services import CrudService
from app.utils import format_date, format_time

# from apps.eridanus.ndb_repository import RunRepository
# from datetime import datetime


class RunningService(CrudService):
    def __init__(self, repository):
        self.repository = repository

    def list(self):
        items = self._fetch()
        records = self._compute_records(items)
        return {'items': items, 'records': records}

    def _fetch(self):
        items = []
        models = self.repository.fetch_all()
        for model in models:
            duration = model.duration
            speed = 'N/A'
            if model.speed:
                speed = model.speed
            else:
                speed = model.distance / (duration / 60.0)

            item = {'duration': duration,
                    'distance': model.distance,
                    'speed': speed,
                    'activity_date': format_date(model.activity_date),
                    'activity_time': format_time(model.activity_time),
                    'calories': model.calories}
            items.append(item)
        return items

    def _compute_records(self, items):
        records = {'max_distance': 0,
                   'max_time': 0,
                   'max_speed': 0.0,
                   'max_calories': 0}
        for item in items:
            if records['max_distance'] < item['distance']:
                records['max_distance'] = item['distance']
            if records['max_time'] < item['duration']:
                records['max_time'] = item['duration']
            if records['max_speed'] < item['speed']:
                records['max_speed'] = item['speed']
            if records['max_calories'] < item['calories']:
                records['max_calories'] = item['calories']
        return records

    def create(self, activity):
        self.repository.create(activity)

    def read(self, activity_id):
        return NotImplemented

    def update(self, activity):
        return NotImplemented

    def delete(self, activity_id):
        return NotImplemented
