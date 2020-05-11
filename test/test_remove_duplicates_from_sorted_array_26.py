from remove_duplicates_from_sorted_array_26 import remove_duplicates
import unittest

class TestRemoveDuplicatesFromSortedArray(unittest.TestCase):

    def test_1(self):
        arr = [1,1,2]
        after_len = remove_duplicates(arr)
        self.assertEqual(after_len, 2)
        self.assertEqual(arr[0], 1)
        self.assertEqual(arr[1], 2)
    
    def test_2(self):
        arr = [0,0,1,1,1,2,2,3,3,4]
        after_len = remove_duplicates(arr)
        self.assertEqual(after_len, 5)
        self.assertEqual(arr[0], 0)
        self.assertEqual(arr[1], 1)
        self.assertEqual(arr[2], 2)
        self.assertEqual(arr[3], 3)
        self.assertEqual(arr[4], 4)

