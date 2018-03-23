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
