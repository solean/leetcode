from remove_element_27 import remove_element
import unittest

class TestRemoveElement(unittest.TestCase):

    def test_1(self):
        arr = [3,2,2,3]
        after_len = remove_element(arr, 3)
        self.assertEqual(after_len, 2)
        self.assertEqual(arr[0], 2)
        self.assertEqual(arr[1], 2)

    def test_2(self):
        arr = [0,1,2,2,3,0,4,2]
        after_len = remove_element(arr, 2)
        self.assertEqual(after_len, 5)
        self.assertEqual(arr[0], 0)
        self.assertEqual(arr[1], 1)
        self.assertEqual(arr[2], 3)
        self.assertEqual(arr[3], 0)
        self.assertEqual(arr[4], 4)

