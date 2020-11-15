from abc import ABCMeta, abstractmethod
from tones.common.exception import ForbiddenSetAttrError


class ValidatorAbstract(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @property
    def caption(self):
        return str(self.__class__.__name__).replace('Validator', '')

    @caption.setter
    def caption(self, caption: str):
        self._caption = caption

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise ForbiddenSetAttrError(key)
        self.__dict__[key] = value
