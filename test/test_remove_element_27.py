from remove_element_27 import remove_element
import unittest

class TestRemoveElement(unittest.TestCase):

    def test_1(self):
        arr = [3,2,2,3]
        after_len = remove_element(arr, 3)
        self.assertEquals(after_len, 2)
        self.assertEquals(arr[0], 2)
        self.assertEquals(arr[1], 2)

    def test_2(self):
        arr = [0,1,2,2,3,0,4,2]
        after_len = remove_element(arr, 2)
        self.assertEquals(after_len, 5)
        self.assertEquals(arr[0], 0)
        self.assertEquals(arr[1], 1)
        self.assertEquals(arr[2], 3)
        self.assertEquals(arr[3], 0)
        self.assertEquals(arr[4], 4)

