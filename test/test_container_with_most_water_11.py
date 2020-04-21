from container_with_most_water_11 import max_area
import unittest

class TestMaxArea(unittest.TestCase):

    def test_1(self):
        self.assertEqual(max_area([1,8,6,2,5,4,8,3,7]), 49)

