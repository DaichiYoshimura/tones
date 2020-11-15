from tones.common.abstract.command import CommandAbstract
from tones.common.mixin.command import CommandMixIn
from tones.tonality.serializer import *
from tones.tonality.validator import *
from tones.tonality.entity import TonalityEntity


class Tonality(CommandMixIn, CommandAbstract):

    def __init__(self, key: str, tonal: str):
        """
        key : Concert keys such as 'C','D+','E-',....
        tonal : 'Major' or 'minor' .
        """

        # Composition Classes
        self._entity: 'TonalityEntity' = TonalityEntity()

        # Initial Props
        self.tonal = tonal
        self.key = key

    # Public Props*****************************************************

    @property
    def tonal(self) -> str:
        return TonalSerializer().to_symbol(self._tonal)

    @tonal.setter
    def tonal(self, symbol: str):
        TonalValidator(symbol)
        self._tonal = TonalSerializer().to_number(symbol)
        self._enharmonic = False

    @property
    def key(self) -> str:
        return KeySerializer(self._tonal).to_symbol(self._key, self._enharmonic)

    @key.setter
    def key(self, symbol: str):
        KeyValidator(symbol, self._tonal)
        number, enharmonic = KeySerializer(self._tonal).to_number(symbol)
        self._key = number
        self._enharmonic = enharmonic

    @property
    def transposed(self) -> float:
        return self._transposed

    @property
    def enharmonic(self) -> bool:
        return self._enharmonic

    # Public Methods*******************************************************

    def convert_tonal(self):
        """
        tonal conversion
        If current tonal is Major, set minor.
        Or minor, set Major.
        """
        self._tonal = TonalSerializer().convert(self._tonal)
        self._enharmonic = False


    def transpose_key(self, number: float):
        """
        key transpose
        input number by 0.5 means half tone.
        """

        ChromatoneValidator(number)
        self._key = KeySerializer(self._tonal).transpose(number, self._key)
        self._transposed = number
        self._enharmonic = False


    def display(self):
        """
        display set attributes
        """

        return {
            'key': self.key,
            'tonal': self.tonal,
            'transposed': self.transposed,
            'enharmonic': self.enharmonic
        }

    # Deligation Props ************************************************

    @property
    def _tonal(self) -> int:
        return self._entity.tonal

    @_tonal.setter
    def _tonal(self, number: int):
        self._entity.tonal = number

    @property
    def _key(self) -> float:
        return self._entity.key

    @_key.setter
    def _key(self, number: float):
        self._entity.key = number

    @property
    def _enharmonic(self) -> bool:
        return self._entity.enharmonic

    @_enharmonic.setter
    def _enharmonic(self, enharmonic: bool):
        self._entity.enharmonic = enharmonic

    @property
    def _transposed(self) -> float:
        return self._entity.transposed

    @_transposed.setter
    def _transposed(self, number: float):
        self._entity.transposed = number
