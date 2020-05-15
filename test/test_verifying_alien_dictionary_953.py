from verifying_alien_dictionary_953 import VerifyingAlienDictionary
import unittest

verifier = VerifyingAlienDictionary()

class TestIsAlienSorted(unittest.TestCase):

    def test_1(self):
        words = ['hello', 'leetcode']
        order = 'hlabcdefgijkmnopqrstuvwxyz'

        self.assertTrue(verifier.is_alien_sorted(words, order))

    def test_2(self):
        words = ['word', 'world', 'row']
        order = 'worldabcefghijkmnpqstuvxyz'

        self.assertFalse(verifier.is_alien_sorted(words, order))

    def test_3(self):
        words = ['apple', 'app']
        order = 'abcdefghijklmnopqrstuvwxyz'

        self.assertFalse(verifier.is_alien_sorted(words, order))

