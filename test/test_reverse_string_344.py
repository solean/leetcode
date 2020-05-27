from reverse_string_344 import reverse_string
import unittest

class TestReverseString(unittest.TestCase):

    def test_1(self):
        s = ['h', 'e', 'l', 'l', 'o']
        expected = ['o', 'l', 'l', 'e', 'h']
        self.assertCountEqual(s, expected)

    def test_2(self):
        s = ['H', 'a', 'n', 'n', 'a', 'h']
        expected = ['h', 'a', 'n', 'n', 'a', 'H']
        self.assertCountEqual(s, expected)

