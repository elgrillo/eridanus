from abc import ABCMeta, abstractmethod
import six
# import warnings


@six.add_metaclass(ABCMeta)
class CrudService(object):

    @abstractmethod
    def fetch_all(self, username):
        return NotImplemented

    @abstractmethod
    def create(self, activity):
        return NotImplemented

    @abstractmethod
    def read(self, activity_id):
        return NotImplemented

    @abstractmethod
    def update(self, activity):
        return NotImplemented

    @abstractmethod
    def delete(self, activity_id):
        return NotImplemented


class BmiCalculatorService():

    UNDERWEIGHT = "Underweight"
    NORMAL = "Normal"
    OVERWEIGHT = "Overweight"
    OBESE = "Obese"

    def __init__(self, weight, height):
        if weight is None:
            self.weight = 0.0
        else:
            self.weight = float(weight)

        if height is None:
            self.height = 0.0
        else:
            self.height = float(height)
        self.bmi = self._calculate_bmi()
        self.status = self._get_status()

    def _calculate_bmi(self):
        '''
        weight (kg)
        height (m)
        '''
        if self.height == 0.0:
            return 0.0

        return self.weight / pow(self.height, 2)

    def calculate_desired_weight(self, bmi):
        return float(bmi) * pow(self.height, 2)

    def _get_status(self):
        if self.bmi < 18.5:
            return BmiCalculatorService.UNDERWEIGHT
        elif self.bmi >= 18.5 and self.bmi < 25:
            return BmiCalculatorService.NORMAL
        elif self.bmi >= 25.0 and self.bmi < 29.9:
            return BmiCalculatorService.OVERWEIGHT
        else:
            return BmiCalculatorService.OBESE
