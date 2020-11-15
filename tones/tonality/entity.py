from typing import Any, Dict
from tones.common.abstract.entity import EntityAbstract
from tones.common.mixin.entity import EntityMixIn


class TonalityEntity(EntityMixIn, EntityAbstract):

    def __init__(self):
        self.tonal = None
        self.key = None
        self.transposed = 0.0
        self.enharmonic = False
        
    @property
    def tonal(self) -> int:
        return self._tonal

    @tonal.setter
    def tonal(self, tonal: int):
        self._tonal = tonal
    
    @property
    def key(self) -> int:
        return self._key

    @key.setter
    def key(self, key: int):
        self._key = key

    @property
    def transposed(self) -> float:
        return self._transposed

    @transposed.setter
    def transposed(self, transposed: float):
        self._transposed = transposed

    @property
    def enharmonic(self) -> bool:
        return self._enharmonic

    @enharmonic.setter
    def enharmonic(self, enharmonic: bool):
        self._enharmonic = enharmonic
    
    