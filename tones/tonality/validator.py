from tones.common.abstract.validator import ValidatorAbstract
from tones.common.mixin.validator import ValidatorMixIn
from tones.tonality.mapper import *


class TonalValidator(ValidatorMixIn, ValidatorAbstract):

    def __init__(self, symbol: str):
        self.execute(symbol)

    def execute(self, symbol: str):
        self.is_required(symbol, self.caption)
        self.is_type_of(symbol, str, self.caption)
        self.is_include_of(symbol, TonalMapper().value_list(), self.caption)


class KeyValidator(ValidatorMixIn, ValidatorAbstract):

    def __init__(self, symbol: str, tonal: int):
        self.execute(symbol, tonal)

    def execute(self, symbol: str, tonal: int):
        self.is_required(symbol, self.caption)
        self.is_type_of(symbol, str, self.caption)
        self.is_include_of(symbol, KeyMapper(tonal).value_list(), self.caption)


class ChromatoneValidator(ValidatorMixIn, ValidatorAbstract):

    def __init__(self, symbol: float):
        self.execute(symbol)

    def execute(self, number: float):
        self.is_required(number, self.caption)
        self.is_type_of(number, float, self.caption)
        self.is_include_of(abs(number), ChromatoneMapper().value_list(), self.caption)
