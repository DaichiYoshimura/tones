from tones.common.exception import IncludeError, MyTypeError, RequiredError
from tones.tonality.validator import ChromatoneValidator, KeyValidator, TonalValidator
import unittest


class TestTonalValidator(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.target_class = TonalValidator

    def test_tonal_exact(self):

        patterns = [
            ('Major', None),
            ('minor', None)
        ]

        for target, expected in patterns:
            with self.subTest(target=target, expected=expected):
                actual = None
                try:
                    self.target_class(target)
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)

    def test_tonal_exception(self):

        error_caption = 'Tonal'
        patterns = [
            (None, str(RequiredError(error_caption))),
            (1, str(MyTypeError(error_caption, str, int))),
            ('Ionian', str(IncludeError(error_caption, 'Ionian')))
        ]

        for target, expected in patterns:
            with self.subTest(target=target, expected=expected):
                actual = None
                try:
                    self.target_class(target)
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)


class TestKeyValidator(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.target_class = KeyValidator

    def test_key_exact(self):

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

    def test_key_exception(self):

        error_caption = 'Key'
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


class TestChromatoneValidator(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.target_class = ChromatoneValidator

    def test_chromatone_exact(self):

        patterns = [
            (0.0, None),
            (0.5, None),
            (1.0, None),
            (1.5, None),
            (2.0, None),
            (2.5, None),
            (3.0, None),
            (3.5, None),
            (4.0, None),
            (4.5, None),
            (5.0, None),
            (5.5, None),
            (-0.5, None),
            (-1.0, None),
            (-1.5, None),
            (-2.0, None),
            (-2.5, None),
            (-3.0, None),
            (-3.5, None),
            (-4.0, None),
            (-4.5, None),
            (-5.0, None),
            (-5.5, None)
        ]

        for target, expected in patterns:
            with self.subTest(target=target, expected=expected):
                actual = None
                try:
                    self.target_class(target)
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)

    def test_chromatone_exception(self):

        error_caption = 'Chromatone'
        patterns = [
            (None, str(RequiredError(error_caption))),
            ('1', str(MyTypeError(error_caption, float, str))),
            (6.0, str(IncludeError(error_caption, '6.0'))),
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
