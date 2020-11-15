from tones.tonality.command import Tonality
import unittest


class TestTonality(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.target_class = Tonality

    def test_convert_tonal(self):

        patterns = [
            ('C', 'Major', 'minor'),
            ('C', 'minor', 'Major'),
        ]

        for key, tonal, expected in patterns:
            with self.subTest(key=key, tonal=tonal, expected=expected):
                actual = None
                try:
                    t = self.target_class(key, tonal)
                    t.convert_tonal()
                    actual = t.tonal
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)
    
    def test_transpose_key(self):

        patterns = [
            ('C', 'Major', 1.0, 'D'),
            ('C', 'minor', 1.0, 'D'),
        ]

        for key, tonal, transpose, expected in patterns:
            with self.subTest(key=key, tonal=tonal, transpose=transpose, expected=expected):
                actual = None
                try:
                    t = self.target_class(key, tonal)
                    t.transpose_key(transpose)
                    actual = t.key
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)

    def test_display(self):

        patterns = [
            ('C', 'Major',{'tonal':'Major','key':'C','enharmonic':False,'transposed':0}),
            ('C', 'minor',{'tonal':'minor','key':'C','enharmonic':False,'transposed':0}),
        ]

        for key, tonal,expected in patterns:
            with self.subTest(key=key, tonal=tonal, expected=expected):
                actual = None
                try:
                    t = self.target_class(key, tonal)
                    actual = t.display()
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
