from two_sum_1 import twoSum
import unittest

class TestTwoSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(twoSum([1, 2, 7, 11, 15], 9), [1, 2])

    def test_2(self):
        self.assertEqual(twoSum([3, 2, 4], 6), [1, 2])


if __name__ == '__main__':
    unittest.main()

