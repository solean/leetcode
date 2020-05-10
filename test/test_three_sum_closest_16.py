from three_sum_closest_16 import three_sum_closest
import unittest

class TestThreeSumClosest(unittest.TestCase):

    def test_1(self):
        nums = [-1, 2, 1, -4]
        target = 1

        self.assertEquals(three_sum_closest(nums, target), 2)

