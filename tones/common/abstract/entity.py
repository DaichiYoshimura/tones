from abc import ABCMeta, abstractmethod
from typing import Any, Dict

class EntityAbstract(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, *args, **kwargs):
       pass
