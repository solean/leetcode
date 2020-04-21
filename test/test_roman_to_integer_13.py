from roman_to_integer_13 import romanToInt
import unittest

class TestRomanToInt(unittest.TestCase):
    def test_1(self):
        self.assertEqual(romanToInt('III'), 3)
    def test_2(self):
        self.assertEqual(romanToInt('IV'), 4)
    def test_3(self):
        self.assertEqual(romanToInt('IX'), 9)
    def test_4(self):
        self.assertEqual(romanToInt('LVIII'), 58)
    def test_5(self):
        self.assertEqual(romanToInt('MCMXCIV'), 1994)

