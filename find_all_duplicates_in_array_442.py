from typing import List
import unittest

def findDuplicates(nums: List[int]) -> List[int]:
    char_map = dict()
    multiples = set()
    
    for n in nums:
        if n in char_map:
            multiples.add(n)
        else:
            char_map[n] = True
    
    return list(multiples)
    

def findDuplicatesWithoutUsingSpace(nums: List[int]) -> List[int]:
    multiples = []

    for n in nums:
        entry = abs(n) - 1
        if nums[entry] < 0:
            multiples.append(abs(n))
        nums[entry] *= -1

    return multiples



class TestFindDuplicates(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(findDuplicates([4,3,2,7,8,2,3,1]), [2,3])

    def test_1_without_using_space(self):
        self.assertEqual(findDuplicatesWithoutUsingSpace([4,3,2,7,8,2,3,1]), [2,3])


if __name__ == '__main__':
    unittest.main()
