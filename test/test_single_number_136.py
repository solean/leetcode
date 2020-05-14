from single_number_136 import single_number
import unittest

class TestSingleNumber(unittest.TestCase):

    def test_1(self):
        self.assertEqual(single_number([2, 2, 1]), 1)

    def test_2(self):
        self.assertEqual(single_number([4, 1, 2, 1, 2]), 4)

