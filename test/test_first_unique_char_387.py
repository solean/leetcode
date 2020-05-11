from first_unique_char_387 import first_unique_char
import unittest

class TestFirstUniqueChar(unittest.TestCase):

    def test_1(self):
        self.assertEqual(first_unique_char('leetcode'), 0)
    
    def test_2(self):
        self.assertEqual(first_unique_char('loveleetcode'), 2)

    def test_no_unique_chars(self):
        self.assertEqual(first_unique_char('aahh'), -1)

