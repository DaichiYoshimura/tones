from tones.tonality.serializer import KeySerializer, TonalSerializer
import unittest


class TestTonalSerializer(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.target_class = TonalSerializer

    def test_to_number(self):

        patterns = [
            ('Major', 0),
            ('minor', 1),
        ]

        for target, expected in patterns:
            with self.subTest(target=target, expected=expected):
                actual = None
                try:
                    actual = self.target_class().to_number(target)
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)

    def test_to_symbol(self):

        patterns = [
            (0, 'Major'),
            (1, 'minor'),
        ]

        for target, expected in patterns:
            with self.subTest(target=target, expected=expected):
                actual = None
                try:
                    actual = self.target_class().to_symbol(target)
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)

    def test_convert(self):

        patterns = [
            (0, 1),
            (1, 0),
        ]

        for target, expected in patterns:
            with self.subTest(target=target, expected=expected):
                actual = None
                try:
                    actual = self.target_class().convert(target)
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)


class TestKeySerializer(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.target_class = KeySerializer

    def test_to_number(self):

        patterns = [
            ('C', 0, (1, False)),
            ('D-', 0, (2, False)),
            ('D', 0, (3, False)),
            ('E-', 0, (4, False)),
            ('E', 0, (5, False)),
            ('F', 0, (6, False)),
            ('G-', 0, (7, False)),
            ('G', 0, (8, False)),
            ('A-', 0, (9, False)),
            ('A', 0, (10, False)),
            ('B-', 0, (11, False)),
            ('B', 0, (12, False)),
            ('C+', 0, (2, True)),
            ('F+', 0, (7, True)),
            ('C-', 0, (12, True)),
            ('C', 1, (1, False)),
            ('C+', 1, (2, False)),
            ('D', 1, (3, False)),
            ('D+', 1, (4, False)),
            ('E', 1, (5, False)),
            ('F', 1, (6, False)),
            ('F+', 1, (7, False)),
            ('G', 1, (8, False)),
            ('G+', 1, (9, False)),
            ('A', 1, (10, False)),
            ('A+', 1, (11, False)),
            ('B', 1, (12, False)),
            ('E-', 1, (4, True)),
            ('A-', 1, (9, True)),
            ('B-', 1, (11, True)),
        ]

        for target, tonal, expected in patterns:
            with self.subTest(target=target, tonal=tonal, expected=expected):
                actual = None
                try:
                    actual = self.target_class(tonal).to_number(target)
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)

    def test_to_symbol(self):

        patterns = [
            (1, 0, False, 'C'),
            (2, 0, False, 'D-'),
            (3, 0, False, 'D'),
            (4, 0, False, 'E-'),
            (5, 0, False, 'E'),
            (6, 0, False, 'F'),
            (7, 0, False, 'G-'),
            (8, 0, False, 'G'),
            (9, 0, False, 'A-'),
            (10, 0, False, 'A'),
            (11, 0, False, 'B-'),
            (12, 0, False, 'B'),
            (13, 0, True, 'C+'),
            (14, 0, True, 'F+'),
            (15, 0, True, 'C-'),
            (1, 1, False, 'C'),
            (2, 1, False, 'C+'),
            (3, 1, False, 'D'),
            (4, 1, False, 'D+'),
            (5, 1, False, 'E'),
            (6, 1, False, 'F'),
            (7, 1, False, 'F+'),
            (8, 1, False, 'G'),
            (9, 1, False, 'G+'),
            (10, 1, False, 'A'),
            (11, 1, False, 'A+'),
            (12, 1, False, 'B'),
            (13, 1, True, 'E-'),
            (14, 1, True, 'A-'),
            (15, 1, True, 'B-'),
        ]

        for target, tonal, enharmonic, expected in patterns:
            with self.subTest(target=target, tonal=tonal, enharmonic=enharmonic, expected=expected):
                actual = None
                try:
                    actual = self.target_class(tonal).to_symbol(target, enharmonic)
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)

    def test_transpose(self):

        patterns = [
            (0.0, 1, 0, 1),
            (0.5, 1, 0, 2),
            (1.0, 1, 0, 3),
            (1.5, 1, 0, 4),
            (2.0, 1, 0, 5),
            (2.5, 1, 0, 6),
            (3.0, 1, 0, 7),
            (3.5, 1, 0, 8),
            (4.0, 1, 0, 9),
            (4.5, 1, 0, 10),
            (5.0, 1, 0, 11),
            (5.5, 1, 0, 12),
            (-0.5, 1, 0, 12),
            (-1.0, 1, 0, 11),
            (-1.5, 1, 0, 10),
            (-2.0, 1, 0, 9),
            (-2.5, 1, 0, 8),
            (-3.0, 1, 0, 7),
            (-3.5, 1, 0, 6),
            (-4.0, 1, 0, 5),
            (-4.5, 1, 0, 4),
            (-5.0, 1, 0, 3),
            (-5.5, 1, 0, 2),
        ]

        for target, current, tonal, expected in patterns:
            with self.subTest(target=target, current=current, tonal=tonal, expected=expected):
                actual = None
                try:
                    actual = self.target_class(tonal).transpose(target, current)
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
