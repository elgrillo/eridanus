from models import Crunch, Run, Weight, PushUp
from datetime import datetime

class Repository(object):
    def __init__(self):
        #self.da = da
        pass

class RunRepository(Repository):
    def __init__(self):
        super(RunRepository, self).__init__()

    def fetch_all(self):
        ''' fetch data from data store '''
        query = Run.query()
        return query.order(-Run.creation_datetime).fetch()
    
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
        run.put()

class WeightRepository(Repository):
    def __init__(self):
        super(WeightRepository, self).__init__()

    def fetch_all(self):
        return Weight.query().fetch()


class PushUpsRepository(Repository):

    def __init__(self):
        super(PushUpsRepository, self).__init__()

    def fetch_all(self):
         ''' fetch data from data store '''
         query = PushUp.query()
         return query.order(-PushUp.creation_datetime).fetch()

    def create(self, dict):
        model = PushUp()
        model.usernickname = dict['user_nickname']
        model.activity_date = dict['activity_date']
        model.activity_time = dict['activity_time']
        model.duration = dict['duration']
        model.calories = dict['calories']
        model.count = dict['count']
        model.notes = dict['notes']
        model.creation_datetime = datetime.now();
        model.put()
        
        
class CrunchesRepository(Repository):
    
    def __init__(self):
        super(CrunchesRepository, self).__init__()
    
    def fetch_all(self):
        query = Crunch.query()
        return query.order(-Crunch.creation_datetime).fetch()
    
    def create(self, dict):
        model = Crunch()
        model.usernickname = dict['user_nickname']
        model.creation_datetime = datetime.now();
        model.activity_date = dict['activity_date']
        model.activity_time = dict['activity_time']
        model.duration = dict['duration']
        model.calories = dict['calories']
        model.count = dict['count']
        model.notes = dict['notes']
        model.put()
        
            
