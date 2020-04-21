from find_all_duplicates_in_array_442 import findDuplicates, findDuplicatesWithoutUsingSpace
import unittest

class TestFindDuplicates(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(findDuplicates([4,3,2,7,8,2,3,1]), [2,3])

    def test_1_without_using_space(self):
        self.assertEqual(findDuplicatesWithoutUsingSpace([4,3,2,7,8,2,3,1]), [2,3])

