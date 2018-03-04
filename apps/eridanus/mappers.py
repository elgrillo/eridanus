
class ActivityMapper(Object):
	pass


class CrunchMapper(ActivityMapper):
	
	def __init__():
		super(CrunchMapper, self).__init__()

	def to_model(self, viewmodel):
		pass
	
	def to_viewmodel(self, model):
		viewmodel = CrunchViewModel()
		viewmodel.activity_date = model.activity_date.strftime('%d %b %Y')
		viewmodel.activity_time = model.activity_time.strftime('%I:%M %p')
    	viewmodel.duration = model.duration
    	viewmodel.calories = model.calories
    	viewmodel.notes = model.notes
    	viewmodel.number_of_exercises = model.number_of_exercises