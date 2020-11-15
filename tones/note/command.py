from tones.common.mixin.command import CommandMixIn
from tones.common.abstract.command import CommandAbstract
from tones.note.serializer import *
from tones.note.validator import *
from tones.note.entity import NoteEntity
from tones.tonality.command import Tonality
from tones.time.command import Time


class Note(CommandMixIn, CommandAbstract):

    def __init__(self, pitch: str, octave: int, duration: str, tonality: 'Tonality', time: 'Time'):
        """
        Before initializing this, You have to instantiate tonality and time class.  
        """

        # Composition Classes
        self._entity: 'NoteEntity' = NoteEntity()
        self._tonality: 'Tonality' = tonality
        self._time: 'Time' = time

        # Initial Props
        self.pitch = pitch
        self.octave = octave
        self.duration = duration

    # Public Props*************************************************************

    @property
    def pitch(self) -> float:
        return PitchSerializer(self._tonal).to_symbol(self._pitch, self._key)

    @pitch.setter
    def pitch(self, pitch: str):
        PitchValidator(pitch, self._tonal)
        self._pitch, self._enharmonic = PitchSerializer(self._tonal).to_number(pitch)

    @property
    def octave(self) -> int:
        return self._octave

    @octave.setter
    def octave(self, octave: int):
        OctaveValidator(octave)
        self._octave = OctaveSerializer().adopt_transpose(octave, self._pitch, self._transposed)

    @property
    def duration(self) -> float:
        return DurationSerialier().to_symbol(self._duration)

    @duration.setter
    def duration(self, duration: str):
        DurationValidator(duration)
        self._duration = DurationSerialier().to_number(duration)

    # Public Methods***************************************************************

    def degree(self) -> float:
        return PitchSerializer(self._tonal).to_degree(self._pitch, self._key)

    def display(self):
        """
        display set attributes
        """

        return {
            'pitch': self.pitch,
            'octave': self.octave,
            'duration': self.duration,
        }

    # Deligation Props*******************************************************

    @property
    def _pitch(self) -> float:
        return self._entity.pitch

    @_pitch.setter
    def _pitch(self, pitch: float):
        self._entity.pitch = pitch

    @property
    def _octave(self) -> int:
        return self._entity.octave

    @_octave.setter
    def _octave(self, octave: int):
        self._entity.octave = octave

    @property
    def _duration(self) -> float:
        return self._entity.duration

    @_duration.setter
    def _duration(self, duration: float):
        self._entity.duration = duration

    @property
    def _sign(self) -> float:
        return self._entity.sign

    @_sign.setter
    def _sign(self, sign: float):
        self._entity.sign = sign

    @property
    def _enharmonic(self) -> bool:
        return self._entity.enharmonic

    @_enharmonic.setter
    def _enharmonic(self, enharmonic: bool):
        self._entity.enharmonic = enharmonic

    @property
    def _tonal(self) -> int:
        return self._tonality._entity.tonal

    @property
    def _key(self) -> float:
        return self._tonality._entity.key

    @property
    def _transposed(self) -> float:
        return self._tonality._entity.transposed

    @property
    def _beats(self) -> float:
        return self._time._entity.beats

    @property
    def _beat_type(self) -> float:
        return self._time._entity.beat_type
