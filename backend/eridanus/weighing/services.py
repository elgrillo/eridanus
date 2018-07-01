from eridanus.repository import WeightRepository
from ..services import CrudService
from ..utils import format_date


class WeighingService(CrudService):

    def __init__(self):
        self.repository = WeightRepository()

    def fetch(self, id):
        return self.repository.fetch(id)

    def fetch_all(self, username):
        min_weight = None
        items = []
        models = self.repository.fetch_all(username)
        for m in models:
            if min_weight is None or min_weight > m.weight:
                min_weight = m.weight
            items.append(
                {
                    'urlsafe': m.key.urlsafe(),
                    'weight': m.weight,
                    'weighing_date': format_date(m.weighing_date)
                })
        return {'items': items, 'min_weight': min_weight}

    def create(self, weighing):
        return self.repository.create(weighing)

    def read(self, urlsafe):
        return self.repository.read(urlsafe)

    def update(self, weighing):
        return self.repository.update(weighing)

    def delete(self, id):
        return self.repository.delete(id)
