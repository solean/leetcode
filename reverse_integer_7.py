import unittest

def reverse_integer(x: int) -> int:
    is_negative = x < 0
    s = str(x)
    r = ''

    if len(s) and s[0] == '-':
        s = s[1:]

    for i in range(len(s) - 1, -1, -1):
        r += s[i]

    n = int(r)
    if n > 2**31 - 1:
        return 0

    if is_negative:
        n *= -1

    return n



class TestReverseInteger(unittest.TestCase):

    def test_standard(self):
        self.assertEqual(reverse_integer(123), 321)

    def test_negative(self):
        self.assertEqual(reverse_integer(-123), -321)

    def test_leading_zero(self):
        self.assertEqual(reverse_integer(120), 21)


if __name__ == '__main__':
    unittest.main()
