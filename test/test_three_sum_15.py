from three_sum_15 import three_sum
import unittest

class TestThreeSum(unittest.TestCase):

    def test_1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected = {
            (-1, 0, 1),
            (-1, -1, 2)
        }
        self.assertEquals(three_sum(nums), expected)

