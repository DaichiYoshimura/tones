from typing import Any, Dict
from tones.common.abstract.entity import EntityAbstract
from tones.common.mixin.entity import EntityMixIn


class NoteEntity(EntityMixIn, EntityAbstract):

    def __init__(self):
        self.pitch = None
        self.octave = None
        self.duration = None
        self.sign = None
        self.enharmonic = False
        
    @property
    def pitch(self) -> float:
        return self._pitch

    @pitch.setter
    def pitch(self, pitch: float):
        self._pitch = pitch

    @property
    def octave(self) -> int:
        return self._octave

    @octave.setter
    def octave(self, octave: int):
        self._octave = octave

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: int):
        self._duration = duration

    @property
    def enharmonic(self) -> bool:
        return self._enharmonic

    @enharmonic.setter
    def enharmonic(self, enharmonic: bool):
        self._enharmonic = enharmonic
