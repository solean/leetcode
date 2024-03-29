from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    seen = {}
    
    for i in range(len(nums)):
        n = nums[i]
        if n in seen:
            return True
        else:
            seen[n] = True
    
    return False

