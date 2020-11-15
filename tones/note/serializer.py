from typing import Tuple
from tones.common.abstract.serializer import SerializerAbstract
from tones.common.mixin.serializer import SerializerMixIn
from tones.note.mapper import *


class PitchSerializer(SerializerMixIn, SerializerAbstract):

    def __init__(self, tonal: int):
        self.pitch_map = PitchMapper(tonal)
        self.enharmonic_map = EnharmonicMapper(tonal)

    def to_number(self, symbol: str) -> Tuple[int, bool]:
        raw_number = self.pitch_map.key_of(symbol)
        enharmonic_number = self.enharmonic_map.get(raw_number)
        is_enharmonic = (enharmonic_number is not None)
        number = enharmonic_number if is_enharmonic else raw_number
        return (number, is_enharmonic)

    def to_symbol(self, number: float, enharmonic: bool) -> str:
        key = self.pitch_map.key_of(number, number) if enharmonic else number
        return self.pitch_map.value_of(key)

    def to_degree(self, number: int, key: int):
        return DegreeMapper(key).value_of(number)


class OctaveSerializer(SerializerMixIn, SerializerAbstract):

    def adopt_transpose(self, octave: int, pitch: float, transposed: float) -> int:
        if pitch + transposed < 0.5:
            octave = octave - 1
        if pitch + transposed > 5.5:
            octave = octave + 1
        return octave


class DurationSerialier(SerializerMixIn, SerializerAbstract):

    def __init__(self):
        self.duration_map = DurationMapper()

    def to_number(self, symbol: str) -> float:
        return self.duration_map.value_of(symbol)

    def to_symbol(self, number: float) -> str:
        return self.duration_map.key_of(number)
