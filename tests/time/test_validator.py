from tones.common.exception import RequiredError, MyTypeError, NaturalError
from tones.time.validator import BeatTypeValidator, BeatsValidator
import unittest


class TestBeatsValidator(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.target_class = BeatsValidator

    def test_beats_exact(self):

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

    def test_beats_exception(self):

        patterns = [
            (None, str(RequiredError('Beats'))),
            (-4, str(NaturalError('Beats'))),
            ('4', str(MyTypeError('Beats', int, str)))
        ]

        for target, expected in patterns:
            with self.subTest(target=target, expected=expected):
                actual = None
                try:
                    self.target_class(target)
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)


class TestBeatTypeValidator(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.target_class = BeatTypeValidator

    def test_beat_type_exact(self):

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

    def test_beat_type_exception(self):

        patterns = [
            (None, str(RequiredError('BeatType'))),
            (-4, str(NaturalError('BeatType'))),
            ('4', str(MyTypeError('BeatType', int, str)))
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
