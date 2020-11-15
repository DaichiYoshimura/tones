from tones.common.abstract.mapper import MapperAbstract
from tones.common.mixin.mapper import MapperMixIn


class TonalMapper(MapperMixIn, MapperAbstract):

    """
    key: tonal number
    value : tonal symbol
    """

    _TONAL = {
        0: 'Major',
        1: 'minor'
    }

    def __init__(self):
        super().__init__(self._TONAL)


class ChromatoneMapper(MapperMixIn, MapperAbstract):

    """
    key : key number
    value : key degree
    key center : key center number
    """

    _CHROMATONE = {
        1: 0.0,
        2: 0.5,
        3: 1.0,
        4: 1.5,
        5: 2.0,
        6: 2.5,
        7: 3.0,
        8: 3.5,
        9: 4.0,
        10: 4.5,
        11: 5.0,
        12: 5.5
    }

    def __init__(self, key_center: int = 1):
        decided = self._generate(key_center)
        super().__init__(decided)

    def _generate(self, key_center):
        keys = dict({x: self._transpose(x, key_center) for x in range(1, 13)})
        return dict({x: self._CHROMATONE.get(keys.get(x)) for x in range(1, 13)})

    def _transpose(self, x, key_center):
        diff = x - key_center + 1
        return diff if diff > 0 else diff + 12

class DegreeMapper(MapperMixIn, MapperAbstract):

    """
    key : key number
    value : key degree
    key center : key center number
    """

    _DEGREE = {
        1: 1.0,
        2: 1.5,
        3: 2.0,
        4: 2.5,
        5: 3.0,
        6: 4.0,
        7: 4.5,
        8: 5.0,
        9: 5.5,
        10: 6.0,
        11: 6.5,
        12: 7.0
    }

    def __init__(self, key_center: int = 1):
        decided = self._generate(key_center)
        super().__init__(decided)

    def _generate(self, key_center):
        keys = dict({x: self._transpose(x, key_center) for x in range(1, 13)})
        return dict({x: self._DEGREE.get(keys.get(x)) for x in range(1, 13)})

    def _transpose(self, x, key_center):
        diff = x - key_center + 1
        return diff if diff > 0 else diff + 12


class PitchMapper(MapperMixIn, MapperAbstract):

    _MAJOR = {
        1: 'C',
        2: 'D-',
        3: 'D',
        4: 'E-',
        5: 'E',
        6: 'F',
        7: 'G-',
        8: 'G',
        9: 'A-',
        10: 'A',
        11: 'B-',
        12: 'B',
        13: 'C+',
        14: 'F+',
        15: 'C-'
    }

    _MINOR = {
        1: 'C',
        2: 'C+',
        3: 'D',
        4: 'D+',
        5: 'E',
        6: 'F',
        7: 'F+',
        8: 'G',
        9: 'G+',
        10: 'A',
        11: 'A+',
        12: 'B',
        13: 'E-',
        14: 'A-',
        15: 'B-'
    }

    def __init__(self, tonal: int = 0):
        super().__init__(self._get_map(tonal))

    def _get_map(self, tonal: int):
        return self._MAJOR if tonal == TonalMapper().key_of('Major') else self._MINOR


class EnharmonicMapper(MapperMixIn, MapperAbstract):

    _MAJOR = {
        13: 2,
        14: 7,
        15: 12
    }

    _MINOR = {
        13: 4,
        14: 9,
        15: 11
    }

    def __init__(self, tonal: int = 0):
        super().__init__(self._get_map(tonal))

    def _get_map(self, tonal: int):
        return self._MAJOR if tonal == TonalMapper().key_of('Major') else self._MINOR


class DurationMapper(MapperMixIn, MapperAbstract):

    _SIGN = {
        'whole': 1,
        'half': 1/2,
        'quarter': 1/4,
        'eighth': 1/8,
        'sixteenth': 1/16,
        'thirty-second': 1/32,
        'dotted-half': 3/8,
        'dotted-quarter': 3/16,
        'dotted-eight': 3/32,
        'dotted-sixteenth': 3/64,
        'dotted-thirty-second': 3/128
    }

    def __init__(self):
        super().__init__(self._SIGN)
