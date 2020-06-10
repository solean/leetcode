from first_and_last_position_of_element_sorted_array_34 import search_range
from typing import List
import unittest

class TestSearchRange(unittest.TestCase):

    def test_found(self):
        self.assertEqual(search_range([5,7,7,8,8,10], 8), [3,4])

    def test_not_found(self):
        self.assertEqual(search_range([5,7,7,8,8,10], 6), [-1,-1])

    def test_all_same(self):
        self.assertEqual(search_range([1,1,1,1,1,1,1,1], 1), [0, 7])

    def test_single_element(self):
        self.assertEqual(search_range([1], 1), [0, 0])

    def test_5(self):
        self.assertEqual(search_range([1, 4], 4), [1, 1])
