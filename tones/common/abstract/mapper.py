from abc import ABCMeta, abstractmethod
from tones.common.exception import ForbiddenSetAttrError


class MapperAbstract(dict, metaclass=ABCMeta):

    def __init__(self, target: dict):
        super().__init__(target)

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise ForbiddenSetAttrError(key)
        self.__dict__[key] = value
