from typing import List
import unittest

def longest_common_prefix(strs: List[str]) -> str:
    if strs is None or len(strs) == 0:
        return ''
    elif len(strs) == 1:
        return strs[0]

    prefix = ''
    i = 0

    while i is not None:
        same_ch = True
        if len(strs[0]) == 0 or i >= len(strs[0]):
            break
        ch = strs[0][i]
        
        for s in strs[1:]:
            if i < len(s) and s[i] == ch:
                same_ch = True
            else:
                same_ch = False
                i = None
                break

        if same_ch:
            prefix += ch
            i += 1

    return prefix



class TestLongestCommonPrefix(unittest.TestCase):

    def test_standard(self):
        self.assertEqual(longest_common_prefix(['flower', 'flow', 'flight']), 'fl')

    def test_none(self):
        self.assertEqual(longest_common_prefix(['dog', 'racecar', 'car']), '')

    def test_single_char(self):
        self.assertEqual(longest_common_prefix(['c', 'c']), 'c')


if __name__ == '__main__':
    unittest.main()
