from length_of_last_word_58 import length_of_last_word
import unittest

class TestLengthOfLastWord(unittest.TestCase):

    def test_1(self):
        self.assertEqual(length_of_last_word('Hello World'), 5)

    def test_2(self):
        self.assertEqual(length_of_last_word('a '), 1)

    def test_3(self):
        self.assertEqual(length_of_last_word(''), 0)
