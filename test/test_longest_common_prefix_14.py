from longest_common_prefix_14 import longest_common_prefix
import unittest

class TestLongestCommonPrefix(unittest.TestCase):

    def test_standard(self):
        self.assertEqual(longest_common_prefix(['flower', 'flow', 'flight']), 'fl')

    def test_none(self):
        self.assertEqual(longest_common_prefix(['dog', 'racecar', 'car']), '')

    def test_single_char(self):
        self.assertEqual(longest_common_prefix(['c', 'c']), 'c')

