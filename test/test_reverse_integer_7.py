from reverse_integer_7 import reverse_integer
import unittest

class TestReverseInteger(unittest.TestCase):

    def test_standard(self):
        self.assertEqual(reverse_integer(123), 321)

    def test_negative(self):
        self.assertEqual(reverse_integer(-123), -321)

    def test_leading_zero(self):
        self.assertEqual(reverse_integer(120), 21)
