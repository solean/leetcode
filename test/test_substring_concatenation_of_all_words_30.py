from substring_concatenation_of_all_words_30 import find_substring
import unittest

class TestSubstringConcatenationOfAllWords(unittest.TestCase):

    def test_1(self):
        s = 'barfoothefoobarman'
        words = ['foo', 'bar']
        self.assertCountEqual(find_substring(s, words), [0, 9])

    def test_2(self):
        s = 'wordgoodgoodgoodbestword'
        words = ['word', 'good', 'best', 'word']
        self.assertCountEqual(find_substring(s, words), [])

    def test_3(self):
        s = 'barfoofoobarthefoobarman'
        words = ['bar', 'foo', 'the']
        self.assertCountEqual(find_substring(s, words), [6, 9, 12])

    def test_4(self):
        s = 'wordgoodgoodgoodbestword'
        words = ['word', 'good', 'best', 'good']
        self.assertCountEqual(find_substring(s, words), [8])

    def test_5(self):
        s = 'lingmindraboofooowingdingbarrwingmonkeypoundcake'
        words = ['fooo', 'barr', 'wing', 'ding', 'wing']
        self.assertCountEqual(find_substring(s, words), [13])

    def test_6(self):
        s = ''
        words = []
        self.assertCountEqual(find_substring(s, words), [])

