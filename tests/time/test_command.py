from tones.time.command import Time
import unittest

class TestTime(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.target_class = Time

    def test_display(self):

        patterns = [
            (4, 4,{'beats':4,'beat_type':4}),
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
