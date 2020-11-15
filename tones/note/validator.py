from tones.common.abstract.validator import ValidatorAbstract
from tones.common.mixin.validator import ValidatorMixIn
from tones.note.mapper import *


class PitchValidator(ValidatorMixIn, ValidatorAbstract):

    def __init__(self, symbol: str, tonal: int):
        self.execute(symbol, tonal)

    def execute(self, symbol: str, tonal: int):
        self.is_required(symbol, self.caption)
        self.is_type_of(symbol, str, self.caption)
        self.is_include_of(symbol, PitchMapper(tonal).value_list(), self.caption)


class OctaveValidator(ValidatorMixIn, ValidatorAbstract):

    def __init__(self, symbol: str):
        self.execute(symbol)

    def execute(self, symbol: str):
        self.is_required(symbol, self.caption)
        self.is_type_of(symbol, int, self.caption)
        self.is_natural(symbol, self.caption)


class DurationValidator(ValidatorMixIn, ValidatorAbstract):

    def __init__(self, symbol: str):
        self.execute(symbol)

    def execute(self, symbol: str):
        self.is_required(symbol, self.caption)
        self.is_type_of(symbol, str, self.caption)
        self.is_include_of(symbol, DurationMapper().key_list(), self.caption)
