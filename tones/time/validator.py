from tones.common.abstract.validator import ValidatorAbstract
from tones.common.mixin.validator import ValidatorMixIn
from tones.time.mapper import *


class BeatsValidator(ValidatorMixIn, ValidatorAbstract):

    def __init__(self, number: int):
        self.execute(number)

    def execute(self, number: int):
        self.is_required(number, self.caption)
        self.is_type_of(number, int, self.caption)
        self.is_natural(number, self.caption)


class BeatTypeValidator(ValidatorMixIn, ValidatorAbstract):

    def __init__(self, number: int):
        self.execute(number)

    def execute(self, number: int):
        self.is_required(number, self.caption)
        self.is_type_of(number, int, self.caption)
        self.is_natural(number, self.caption)
