from datetime import datetime

from eridanus.models import Crunch, Run, Weight, PushUp


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
        return query.order(-Run.activity_date).fetch()

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
                .order(-Weight.weighing_date)
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
        return query.order(-PushUp.activity_date).fetch()

    def fetch(activity_id):
        NotImplemented


class CrunchesRepository(Repository):

    def __init__(self):
        super(CrunchesRepository, self).__init__()

    def fetch_all(self, username):
        query = Crunch.query(Crunch.usernickname == username)
        return query.order(-Crunch.activity_date).fetch()

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


class StatisticsRepository(Repository):

    def __init__(self):
        super(StatisticsRepository, self).__init__()

    def running_stats(self, username):
        avg_calories = 0
        avg_speed = 0.0
        avg_distance = 0.0
        avg_time = 0
        count = 0
        date_last_run = None
        days_from_last_run = 0
        max_calories = 0
        max_distance = 0
        max_speed = 0.0
        max_time = 0
        total_calories = 0
        total_distance = 0
        total_time = 0

        items = (
                Run
                .query(Run.usernickname == username)
                .order(-Run.activity_date)
                .fetch()
            )
        count = len(items)
        if count > 0:
            date_last_run = items[0].activity_date
            days_from_last_run = self._days_from_last_run(
                        date_last_run)
            total_speed = 0
            for item in items:
                duration = item.duration
                if item.calories:
                    total_calories += item.calories
                    if item.calories > max_calories:
                        max_calories = item.calories
                total_distance += item.distance
                total_time += duration
                if item.distance > max_distance:
                    max_distance = item.distance
                if duration > max_time:
                    max_time = duration
                speed = item.speed
                if item.speed is None:
                    speed = item.distance / (duration / 60.0)
                total_speed += speed
                if speed > max_speed:
                    max_speed = speed
            avg_calories = self._avg(total_calories, count)
            avg_distance = self._avg(total_distance, count)
            avg_time = self._avg(total_time, count)
            avg_speed = self._avg(total_speed, count)
        return {
            'avg_calories': avg_calories,
            'avg_speed': avg_speed,
            'avg_distance': avg_distance,
            'avg_time': avg_time,
            'count': count,
            'date_last_run': date_last_run,
            'days_from_last_run': days_from_last_run,
            'max_calories': max_calories,
            'max_distance': max_distance,
            'max_speed': max_speed,
            'max_time': max_time,
            'total_distance': total_distance,
            'total_time': total_time,
            'total_calories': total_calories
        }

    def _avg(self, total, count):
        return float(total)/float(count)

    def _days_from_last_run(self, date_last_run):
        if date_last_run:
            diff = abs(datetime.now().date() - date_last_run)
            return diff.days
        return None

    def weighing_stats(self, username):
        avg = 0.0
        avg_last20 = 0.0
        count = 0
        growth_rate_last20 = 0.0
        last_weight = 0.0
        min = 0.0
        max = 0.0
        trend = ''

        items = (
                    Weight
                    .query(Weight.usernickname == username)
                    .order(-Weight.weighing_date)
                    .fetch()
                )
        count = len(items)
        if count > 0:
            last_weight = items[0].weight
            total = 0.0
            total_last20 = 0.0
            for i in range(count):
                weight = items[i].weight
                total += weight
                if min > weight:
                    min = weight
                if max < weight:
                    max = weight
                if i <= 19:
                    total_last20 = total
            avg_last20 = self._avg(
                total_last20,
                20.0 if count > 20 else float(count))
            avg = self._avg(total, count)
            if count > 1:
                growth_rate_last20 = self._growth_rate(avg_last20, last_weight)
        return {
            'avg': avg,
            'avg_last20': avg_last20,
            'count': count,
            'growth_rate_last20': growth_rate_last20,
            'last_weight': last_weight,
            'max': max,
            'min': min,
            'trend': trend
        }

    def _growth_rate(self, avg, last):
        # https://www.wikihow.com/Calculate-Growth-Rate
        return ((float(last) / float(avg)) - 1.0) * 100.0
