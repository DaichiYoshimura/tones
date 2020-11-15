from tones.common.abstract.entity import EntityAbstract
from tones.common.mixin.entity import EntityMixIn


class TimeEntity(EntityMixIn, EntityAbstract):

    def __init__(self):
        self.beats = 4
        self.beat_type = 4

    @property
    def beats(self) -> int:
        return self._beats

    @beats.setter
    def beats(self, beats: int):
        self._beats = beats

    @property
    def beat_type(self) -> int:
        return self._beat_type

    @beat_type.setter
    def beat_type(self, beat_type: int):
        self._beat_type = beat_type
