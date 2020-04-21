import unittest

def lengthOfLongestSubstring(s: str) -> int:
    longest = 1
    l = len(s)
    if l == 0:
        return 0
    elif l == 1:
        return 1

    i = 0
    while i < l:
        seen = {}
        for j in range(i, l):
            ch = s[j]
            if ch in seen:
                if j - i > longest:
                    longest = j - i
                break
            elif j == l - 1:
                if j - i + 1 > longest:
                    longest = j - i + 1
            else:
                seen[ch] = True
        i += 1

    return longest



class TestLengthOfLongestSubstring(unittest.TestCase):

    def test_1(self):
        self.assertEqual(lengthOfLongestSubstring('abcabcbb'), 3)

    def test_2(self):
        self.assertEqual(lengthOfLongestSubstring('bbbbb'), 1)

    def test_3(self):
        self.assertEqual(lengthOfLongestSubstring('pwwkew'), 3)

    def test_4(self):
        self.assertEqual(lengthOfLongestSubstring('au'), 2)


if __name__ == '__main__':
    unittest.main()
