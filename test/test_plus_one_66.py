from plus_one_66 import plus_one
import unittest

class TestPlusOne(unittest.TestCase):

    def test_1(self):
        self.assertCountEqual(plus_one([1, 2, 3]), [1, 2, 4])

    def test_2(self):
        self.assertCountEqual(plus_one([4, 3, 2, 1]), [4, 3, 2, 2])

    def test_3(self):
        self.assertCountEqual(plus_one([9, 9]), [1, 0, 0])

    def test_4(self):
        self.assertCountEqual(plus_one([5, 9, 9]), [6, 0, 0])

