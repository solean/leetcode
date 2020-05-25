from maximum_subarray_53 import max_subarray
import unittest

class TestMaximumSubarray(unittest.TestCase):

    def test_1(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(max_subarray(nums), 6)

    def test_2(self):
        nums = [-2, -1]
        self.assertEqual(max_subarray(nums), -1)

    def test_empty(self):
        nums = []
        self.assertEqual(max_subarray(nums), 0)

    def test_single(self):
        nums = [2]
        self.assertEqual(max_subarray(nums), 2)

