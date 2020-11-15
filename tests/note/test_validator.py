from tones.common.exception import IncludeError, MyTypeError, NaturalError, RequiredError
from tones.note.validator import DurationValidator, OctaveValidator, PitchValidator
import unittest


class TestPitchValidator(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.target_class = PitchValidator

    def test_pitch_exact(self):

        patterns = [
            ('C', 0, None),
            ('D-', 0, None),
            ('D', 0, None),
            ('E-', 0, None),
            ('E', 0, None),
            ('F', 0, None),
            ('G-', 0, None),
            ('G', 0, None),
            ('A-', 0, None),
            ('A', 0, None),
            ('B-', 0, None),
            ('B', 0, None),
            ('C+', 0, None),
            ('F+', 0, None),
            ('C-', 0, None),
            ('C', 1, None),
            ('C+', 1, None),
            ('D', 1, None),
            ('D+', 1, None),
            ('E', 1, None),
            ('F', 1, None),
            ('F+', 1, None),
            ('G', 1, None),
            ('G+', 1, None),
            ('A', 1, None),
            ('A+', 1, None),
            ('E', 1, None),
            ('E-', 1, None),
            ('A-', 1, None),
            ('B-', 1, None),
        ]

        for target, tonal, expected in patterns:
            with self.subTest(target=target, tonal=tonal, expected=expected):
                actual = None
                try:
                    self.target_class(target, tonal)
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)

    def test_pitch_exception(self):

        error_caption = 'Pitch'
        patterns = [
            (None, 0, str(RequiredError(error_caption))),
            (1, 0, str(MyTypeError(error_caption, str, int))),
            ('Cm', 0, str(IncludeError(error_caption, 'Cm'))),
            (None, 1, str(RequiredError(error_caption))),
            (1, 1, str(MyTypeError(error_caption, str, int))),
            ('Cm', 1, str(IncludeError(error_caption, 'Cm')))
        ]

        for target, tonal, expected in patterns:
            with self.subTest(target=target, tonal=tonal, expected=expected):
                actual = None
                try:
                    self.target_class(target, tonal)
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)


class TestOctaveValidator(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.target_class = OctaveValidator

    def test_octave_exact(self):

        patterns = [
            (1, None),
            (2, None),
            (3, None),
            (4, None),
            (5, None),
            (6, None),
            (7, None),
            (8, None),
            (9, None),
            (10, None),
            (11, None),
            (12, None),
            (13, None),
            (14, None),
            (15, None)
        ]

        for target, expected in patterns:
            with self.subTest(target=target, expected=expected):
                actual = None
                try:
                    self.target_class(target)
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)

    def test_octave_exception(self):

        error_caption = 'Octave'
        patterns = [
            (None, str(RequiredError(error_caption))),
            (-4, str(NaturalError(error_caption))),
            ('4', str(MyTypeError(error_caption, int, str)))
        ]

        for target, expected in patterns:
            with self.subTest(target=target, expected=expected):
                actual = None
                try:
                    self.target_class(target)
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)


class TestDurationValidator(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.target_class = DurationValidator

    def test_duration_exact(self):

        patterns = [
            ('whole', None),
            ('half', None),
            ('quarter', None),
            ('eighth', None),
            ('sixteenth', None),
            ('thirty-second', None),
            ('dotted-half', None),
            ('dotted-quarter', None),
            ('dotted-eight', None),
            ('dotted-sixteenth', None),
            ('dotted-thirty-second', None)
        ]

        for target, expected in patterns:
            with self.subTest(target=target, expected=expected):
                actual = None
                try:
                    self.target_class(target)
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)

    def test_duration_exception(self):

        error_caption = 'Duration'
        patterns = [
            (None, str(RequiredError(error_caption))),
            (1, str(MyTypeError(error_caption, str, int))),
            ('4', str(IncludeError(error_caption, '4'))),
        ]

        for target, expected in patterns:
            with self.subTest(target=target, expected=expected):
                actual = None
                try:
                    self.target_class(target)
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
