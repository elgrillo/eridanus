from ..utils import format_date, format_time
from ..services import CrudService


class BaseActivityService(CrudService):

    def __init__(self, repository):
        self.repository = repository

    def fetch_all(self, username):
        items = []
        models = self.repository.fetch_all(username)
        if models is not None:
            for model in models:
                item = {'activity_time': format_time(model.activity_time),
                        'activity_date': format_date(model.activity_date),
                        'count': model.count,
                        'calories': model.calories,
                        'duration': model.duration,
                        'notes': model.notes}
                items.append(item)
        return items

    def create(self, activity):
        return self.repository.create(activity)

    def read(self, activity_id):
        return self.repository.read(activity_id)

    def update(self, activity):
        return self.repository.update(activity)

    def delete(self, activity_id):
        return self.repository.delete(activity_id)


class CrunchesService(BaseActivityService):

    def __init__(self):
        from eridanus.repository import CrunchesRepository
        super(CrunchesService, self).__init__(CrunchesRepository())


class JumpRopeService(BaseActivityService):

    def __init__(self):
        from eridanus.repository import JumpRopeRepository
        super(JumpRopeService, self).__init__(JumpRopeRepository())


class PushupsService(BaseActivityService):

    def __init__(self):
        from eridanus.repository import PushUpsRepository
        super(PushupsService, self).__init__(PushUpsRepository())


class RunningService(CrudService):

    def __init__(self):
        from eridanus.repository import RunRepository
        self.repository = RunRepository()

    def fetch_all(self, username):
        items = self._fetch_all(username)
        records = self._compute_records(items)
        return {'items': items, 'records': records}

    def _fetch_all(self, username):
        items = []
        models = self.repository.fetch_all(username)
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
                    'calories': model.calories,
                    'urlsafe': model.key.urlsafe()}
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

    def read(self, activity_urlsafe):
        import logging
        logging.info(
            'Read running entity having url_safe {}'.format(activity_urlsafe))
        return self.repository.read(activity_urlsafe)

    def update(self, activity):
        self.repository.update(activity)

    def delete(self, activity_id):
        self.repository.delete(activity_id)