from remove_duplicates_from_sorted_array_26 import remove_duplicates
import unittest

class TestRemoveDuplicatesFromSortedArray(unittest.TestCase):

    def test_1(self):
        arr = [1,1,2]
        after_len = remove_duplicates(arr)
        self.assertEquals(after_len, 2)
        self.assertEquals(arr[0], 1)
        self.assertEquals(arr[1], 2)
    
    def test_2(self):
        arr = [0,0,1,1,1,2,2,3,3,4]
        after_len = remove_duplicates(arr)
        self.assertEquals(after_len, 5)
        self.assertEquals(arr[0], 0)
        self.assertEquals(arr[1], 1)
        self.assertEquals(arr[2], 2)
        self.assertEquals(arr[3], 3)
        self.assertEquals(arr[4], 4)

