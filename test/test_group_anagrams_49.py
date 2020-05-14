from group_anagrams_49 import group_anagrams
import unittest

class TestGroupAnagrams(unittest.TestCase):

    def test_1(self):
        strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
        expected = [
            ['ate', 'eat', 'tea'],
            ['nat', 'tan'],
            ['bat']
        ]

        groups = group_anagrams(strs)
        self.assertEqual(len(groups), 3)
        for g in groups:
            if len(g) == 3:
                self.assertCountEqual(g, expected[0])
            elif len(g) == 2:
                self.assertCountEqual(g, expected[1])
            elif len(g) == 1:
                self.assertCountEqual(g, expected[2])

    def test_2(self):
        strs = ['cab', 'tin', 'pew', 'duh', 'may', 'ill', 'buy', 'bar', 'max', 'doc']
        expected = [
            ['doc'],
            ['bar'],
            ['buy'],
            ['ill'],
            ['may'],
            ['tin'],
            ['cab'],
            ['pew'],
            ['max'],
            ['duh']
        ]

        self.assertCountEqual(group_anagrams(strs), expected)

