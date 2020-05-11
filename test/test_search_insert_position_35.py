from search_insert_position_35 import search_insert
import unittest

class TestSearchInsertPosition(unittest.TestCase):

    def test_1(self):
        self.assertEqual(search_insert([1,3,5,6], 5), 2)
    
    def test_2(self):
        self.assertEqual(search_insert([1,3,5,6], 2), 1)
    
    def test_3(self):
        self.assertEqual(search_insert([1,3,5,6], 7), 4)
    
    def test_4(self):
        self.assertEqual(search_insert([1,3,5,6], 0), 0)

