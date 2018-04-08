from eridanus.repository import StatisticsRepository


class DashboardService(object):
    ''' statistics class 
    Is this a model class a controller or a controller class? Not very clear
    TODO: to be reviewed
    '''
    # pylint: disable=too-many-instance-attributes
    # TODO maybe I should review this class as it could 
    # have to many responsabilities
    # a run statistic class can be created a weight stats and so on
    # https://softwareengineering.stackexchange.com/questions/302549/how-does-having-too-many-instance-variables-lead-to-duplicate-code
    def __init__(self):
        self.repository = StatisticsRepository()

    def home_stats(self, username):
        running_stats = self.repository.running_stats(username)
        weighing_stats = self.repository.weighing_stats(username)
        return {
            'activities': {
                'running': running_stats
            },
            'weighing': weighing_stats
        }

    # def get_day_from_last_run_class(self):
    #     if self.days_past_from_last_run is None:
    #         return ''
    #     diff = self.days_past_from_last_run
    #     if diff < 3:
    #         return 'label-success'
    #     elif diff < 4:
    #         return 'label-warning'
    #     else:
    #         return 'label-danger'
