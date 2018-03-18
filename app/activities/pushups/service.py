from app.services import CrudService
from app.utils import format_date, format_time


class PushupsService(CrudService):
    ''' Push-ups controller '''

    def __init__(self, repository):
        self.repository = repository

    def list(self):
        ''' creates and returns the view and viewmodel '''
        items = []
        models = self.repository.fetch_all()
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
        self.repository.create(activity)

    def read(self, activity_id):
        return NotImplemented

    def update(self, activity):
        return NotImplemented

    def delete(self, activity_id):
        return NotImplemented
