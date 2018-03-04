from models import Run, Weight

class DataAdapter(object):
    def __init__(self, model):
        pass

class NdbDataAdapter(DataAdapter):
    def __init__(self, model):
        super(DataAdapter, self).__init__(self)

    def fetch_all(self, model):
        return model.query().fetch()

