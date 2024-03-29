from typing import List

def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    l = 0
    product = 1
    count = 0

    for r in range(len(nums)):
        product *= nums[r]

        while l < len(nums) and product >= k:
            product /= nums[l]
            l += 1
        
        count += max(0, 1 + (r - l))
    
    return count
