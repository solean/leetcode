from letter_combinations_of_phone_number_17 import letter_combinations
import unittest

class TestLetterCombinations(unittest.TestCase):

    def test_1(self):
        combinations = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEquals(letter_combinations("23"), combinations)

