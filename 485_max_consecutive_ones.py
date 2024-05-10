from typing import List

def findMaxConsecutiveOnes(nums: List[int]) -> int:
    l, r = 0, 0
    max_cons = 0

    while r < len(nums):
        print(l, r)
        if nums[l] == 1:
            while r < len(nums) and nums[r] == 1:
                r += 1
                max_cons = max(max_cons, r - l)
            l = r
        else:
            l += 1
            r = l
    
    return max_cons
