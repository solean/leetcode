from merge_intervals_56 import merge
import unittest

class TestMergeIntervals(unittest.TestCase):

    def test_1(self):
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        expected = [[1,6],[8,10],[15,18]]
        merged = merge(intervals)
        self.assertCountEqual(merged, expected)

    def test_2(self):
        intervals = [[1,4],[4,5]]
        expected = [[1,5]]
        merged = merge(intervals)
        self.assertCountEqual(merged, expected)

    def test_3(self):
        intervals = [[1,4],[0,4]]
        expected = [[0,4]]
        merged = merge(intervals)
        self.assertCountEqual(merged, expected)

