from palindrome_number_9 import isPalindrome
import unittest

class TestIsPalindrome(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(isPalindrome(121), True)
        self.assertEqual(isPalindrome(10), False)
        self.assertEqual(isPalindrome(1001), True)

    def test_negative(self):
        self.assertEqual(isPalindrome(-121), False)

