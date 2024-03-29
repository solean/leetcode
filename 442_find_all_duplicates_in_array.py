from typing import List

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

