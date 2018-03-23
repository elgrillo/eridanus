from models import Crunch, Run, Weight, PushUp
from datetime import datetime


class Repository(object):
    def __init__(self):
        pass


class RunRepository(Repository):
    def __init__(self):
        super(RunRepository, self).__init__()

    def create(self, dict):
        run = Run()
        run.usernickname = dict['user_nickname']
        run.activity_date = dict['activity_date']
        run.activity_time = dict['activity_time']
        run.duration = dict['duration']
        run.distance = dict['distance']
        run.speed = dict['speed']
        run.calories = dict['calories']
        run.notes = dict['notes']
        run.creation_datetime = datetime.now()
        return run.put()

    def delete(activity_id):
        NotImplemented

    def fetch_all(self, username):
        ''' fetch data from data store '''
        query = Run.query(Run.usernickname == username)
        return query.order(-Run.creation_datetime).fetch()

    def fetch(activity_id):
        NotImplemented

    def update(self, activity):
        NotImplemented


class WeightRepository(Repository):
    def __init__(self):
        super(WeightRepository, self).__init__()

    def fetch(self, id):
        return NotImplemented

    def fetch_all(self, username):
        return (Weight
                .query(Weight.usernickname == username)
                .order(-Weight.creation_datetime)
                .fetch()
                )

    def create(self, weighing):
        w = Weight()
        w.usernickname = weighing['user_nickname']
        w.weight = weighing['weight']
        w.weighing_date = weighing['weighing_date']
        w.creation_datetime = datetime.now()
        return w.put()

    def update(self, update):
        return NotImplemented

    def delete(self, id):
        return NotImplemented


class PushUpsRepository(Repository):

    def __init__(self):
        super(PushUpsRepository, self).__init__()

    def create(self, dict):
        model = PushUp()
        model.usernickname = dict['user_nickname']
        model.activity_date = dict['activity_date']
        model.activity_time = dict['activity_time']
        model.duration = dict['duration']
        model.calories = dict['calories']
        model.count = dict['count']
        model.notes = dict['notes']
        model.creation_datetime = datetime.now()
        return model.put()

    def update(self, activity):
        NotImplemented

    def delete(activity_id):
        NotImplemented

    def fetch_all(self, username):
        ''' fetch data from data store '''
        query = PushUp.query(PushUp.usernickname == username)
        return query.order(-PushUp.creation_datetime).fetch()

    def fetch(activity_id):
        NotImplemented


class CrunchesRepository(Repository):

    def __init__(self):
        super(CrunchesRepository, self).__init__()

    def fetch_all(self, username):
        query = Crunch.query(Crunch.usernickname == username)
        return query.order(-Crunch.creation_datetime).fetch()

    def create(self, dict):
        model = Crunch()
        model.usernickname = dict['user_nickname']
        model.creation_datetime = datetime.now()
        model.activity_date = dict['activity_date']
        model.activity_time = dict['activity_time']
        model.duration = dict['duration']
        model.calories = dict['calories']
        model.count = dict['count']
        model.notes = dict['notes']
        return model.put()

    def read(self, activity_id):
        return NotImplemented

    def update(self, activity):
        return NotImplemented

    def delete(self, activity_id):
        return NotImplemented