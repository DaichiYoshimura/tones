from abc import ABCMeta, abstractmethod
from tones.common.exception import ForbiddenSetAttrError


class SerializerAbstract(metaclass=ABCMeta):

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise ForbiddenSetAttrError(key)
        self.__dict__[key] = value
