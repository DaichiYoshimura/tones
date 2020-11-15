from abc import ABCMeta, abstractmethod
from typing import Any, Dict


class CommandAbstract(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

