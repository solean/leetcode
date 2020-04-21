from median_of_two_sorted_arrays_4 import findMedianSortedArrays
import unittest

class TestFindMedianSortedArrays(unittest.TestCase):

    def test_1(self):
        self.assertEqual(findMedianSortedArrays([1, 3], [2]), 2.0)

    def test_2(self):
        self.assertEqual(findMedianSortedArrays([1, 2], [3, 4]), 2.5)

    def test_3(self):
        self.assertEqual(findMedianSortedArrays([3, 4], [1, 2]), 2.5)

    def test_4(self):
        self.assertEqual(findMedianSortedArrays([1, 2, 2], [1, 2, 3]), 2.0)

