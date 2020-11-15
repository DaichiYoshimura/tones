from tones.common.abstract.command import CommandAbstract
from tones.common.mixin.command import CommandMixIn
from tones.time.serializer import *
from tones.time.validator import *
from tones.time.entity import TimeEntity


class Time(CommandMixIn, CommandAbstract):

    def __init__(self, beats: int, beat_type: int):
        """
        beats : beat count
        beat_type : beat type
        """

        # Composition Classes
        self._entity: 'TimeEntity' = TimeEntity()

        # Initial Props
        self.beats = beats
        self.beat_type = beat_type

    # Public Props*****************************************************

    @property
    def beats(self) -> int:
        return self._beats

    @beats.setter
    def beats(self, beats: int):
        BeatsValidator(beats)
        self._beats = beats

    @property
    def beat_type(self) -> int:
        return self._beat_type

    @beat_type.setter
    def beat_type(self, beat_type: int):
        BeatTypeValidator(beat_type)
        self._beat_type = beat_type

    # Public Methods*******************************************************

    def display(self):
        """
        display set attributes
        """

        return {
            'beats': self.beats,
            'beat_type': self.beat_type
        }

    # Deligation Props*******************************************************

    @property
    def _beats(self) -> int:
        return self._entity.beats

    @_beats.setter
    def _beats(self, beats: int):
        self._entity.beats = beats

    @property
    def _beat_type(self) -> int:
        return self._entity.beat_type

    @_beat_type.setter
    def _beat_type(self, beat_type: int):
        self._entity.beat_type = beat_type
