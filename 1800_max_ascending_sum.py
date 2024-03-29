from typing import List

def max_ascending_sum(nums: List[int]) -> int:
    max_sum = 0
    curr_sum = 0
    prev = 0
    
    for i in range(len(nums)):
        if nums[i] > prev:
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
        else:
            curr_sum = nums[i]
            
        prev = nums[i]
        
    return max_sum
