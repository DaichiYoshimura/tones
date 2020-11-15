import typing
from tones.common.abstract.serializer import SerializerAbstract
from tones.common.mixin.serializer import SerializerMixIn
from tones.tonality.mapper import *


class TonalSerializer(SerializerMixIn, SerializerAbstract):

    def __init__(self):
        self.tonal_map = TonalMapper()

    def to_number(self, symbol: str) -> int:
        return self.tonal_map.key_of(symbol)

    def to_symbol(self, number: int) -> str:
        return self.tonal_map.value_of(number)

    def convert(self, number: int) -> int:
        minor = self.tonal_map.key_of('minor')
        major = self.tonal_map.key_of('Major')
        return minor if major == number else major


class KeySerializer(SerializerMixIn, SerializerAbstract):

    def __init__(self, tonal: int):
        self.key_map = KeyMapper(tonal)
        self.enharmonic_map = EnharmonicMapper(tonal)
        self.chromatone_map = ChromatoneMapper

    def to_number(self, symbol: str) -> typing.Tuple[int, bool]:
        raw_number = self.key_map.key_of(symbol)
        enharmonic_number = self.enharmonic_map.get(raw_number)
        is_enharmonic = (enharmonic_number is not None)
        number = enharmonic_number if is_enharmonic else raw_number
        return (number, is_enharmonic)

    def to_symbol(self, number: float,  enharmonic: bool) -> str:
        key = self.key_map.key_of(number, number) if enharmonic else number
        return self.key_map.value_of(key)

    def transpose(self, additional: float, current: int) -> int:
        if additional < 0.0:
            additional = additional + 6.0
        if additional > 6.0:
            additional = additional - 6.0
        return self.chromatone_map(current).key_of(additional)
