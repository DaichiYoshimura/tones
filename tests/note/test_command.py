from tones.tonality.command import Tonality
from tones.note.command import Note
from tones.time.command import Time
import unittest


class TestNote(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.target_class = Note

    def test_degree(self):

        patterns = [
            (4, 4, 'C', 'Major', 'C', 1, 'quarter', 0.0),
            (4, 4, 'D', 'Major', 'D', 1, 'quarter', 0.0),
            (4, 4, 'C', 'Major', 'D', 1, 'quarter', 1.0),
        ]

        for beats, beat_type, key, tonal, pitch, octave, duration, expected in patterns:
            with self.subTest(beats=beats, beat_type=beat_type, key=key, tonal=tonal, pitch=pitch, octave=octave, duration=duration, expected=expected):
                actual = None
                try:
                    time = Time(beats, beat_type)
                    tonality = Tonality(key, tonal)
                    t = self.target_class(pitch, octave, duration, tonality, time)
                    actual = t.degree()
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)

    def test_display(self):

        patterns = [
            (4, 4, 'C', 'Major', 'C', 1, 'quarter', {'pitch':'C','octave':1,'duration':'quarter'}),
            (4, 4, 'D', 'Major', 'D', 1, 'quarter', {'pitch':'D','octave':1,'duration':'quarter'}),
            (4, 4, 'C', 'Major', 'D', 1, 'quarter', {'pitch':'D','octave':1,'duration':'quarter'}),
        ]

        for beats, beat_type, key, tonal, pitch, octave, duration, expected in patterns:
            with self.subTest(beats=beats, beat_type=beat_type, key=key, tonal=tonal, pitch=pitch, octave=octave, duration=duration, expected=expected):
                actual = None
                try:
                    time = Time(beats, beat_type)
                    tonality = Tonality(key, tonal)
                    t = self.target_class(pitch, octave, duration, tonality, time)
                    actual = t.display()
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
