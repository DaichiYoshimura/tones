from tones.note.serializer import DurationSerialier, OctaveSerializer, PitchSerializer
import unittest

class TestPitchSerializer(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.target_class = PitchSerializer

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

    def test_to_degree(self):

        patterns = [
            (1, 0, 1, 0.0),
            (2, 0, 1, 0.5),
            (3, 0, 1, 1.0),
            (4, 0, 1, 1.5),
            (5, 0, 1, 2.0),
            (6, 0, 1, 2.5),
            (7, 0, 1, 3.0),
            (8, 0, 1, 3.5),
            (9, 0, 1, 4.0),
            (10, 0, 1, 4.5),
            (11, 0, 1, 5.0),
            (12, 0, 1, 5.5)
        ]

        for target, tonal, enharmonic, expected in patterns:
            with self.subTest(target=target, tonal=tonal, enharmonic=enharmonic, expected=expected):
                actual = None
                try:
                    actual = self.target_class(tonal).to_degree(target, enharmonic)
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)

class TestOctaveSerializer(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.target_class = OctaveSerializer
    
    def test_adopt_transpose(self):

        patterns = [
            (1, 1.0, 1.0, 1),
            (1, 0.5, -0.5, 0),
            (1, 12, 0.5, 2)
        ]

        for octave, pitch, transposed, expected in patterns:
            with self.subTest(octave=octave,pitch=pitch,transposed=transposed, expected=expected):
                actual = None
                try:
                    actual = self.target_class().adopt_transpose(octave,pitch,transposed)
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)

class TestDurationSerializer(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.target_class = DurationSerialier
    
    def test_to_number(self):

        patterns = [
            ('whole', 1),
            ('half', 1/2),
            ('quarter', 1/4),
            ('eighth', 1/8),
            ('sixteenth', 1/16),
            ('thirty-second', 1/32),
            ('dotted-half', 3/8),
            ('dotted-quarter', 3/16),
            ('dotted-eight', 3/32),
            ('dotted-sixteenth', 3/64),
            ('dotted-thirty-second', 3/128)
        ]

        for target, expected in patterns:
            with self.subTest(target=target,expected=expected):
                actual = None
                try:
                    actual = self.target_class().to_number(target)
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)
    
    def test_to_symbol(self):

        patterns = [
            (1,'whole'),
            (1/2,'half'),
            (1/4,'quarter'),
            (1/8,'eighth'),
            (1/16,'sixteenth'),
            (1/32,'thirty-second'),
            (3/8,'dotted-half'),
            (3/16,'dotted-quarter'),
            (3/32,'dotted-eight'),
            (3/64,'dotted-sixteenth'),
            (3/128,'dotted-thirty-second')
        ]

        for target, expected in patterns:
            with self.subTest(target=target,expected=expected):
                actual = None
                try:
                    actual = self.target_class().to_symbol(target)
                except Exception as e:
                    actual = str(e)
                self.assertEqual(expected, actual)

    
if __name__ == '__main__':
    unittest.main()
