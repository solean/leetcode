from longest_substring_without_repeat_char_3 import lengthOfLongestSubstring
import unittest

class TestLengthOfLongestSubstring(unittest.TestCase):

    def test_1(self):
        self.assertEqual(lengthOfLongestSubstring('abcabcbb'), 3)

    def test_2(self):
        self.assertEqual(lengthOfLongestSubstring('bbbbb'), 1)

    def test_3(self):
        self.assertEqual(lengthOfLongestSubstring('pwwkew'), 3)

    def test_4(self):
        self.assertEqual(lengthOfLongestSubstring('au'), 2)