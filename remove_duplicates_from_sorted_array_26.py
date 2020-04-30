from typing import List

def remove_duplicates(nums: List[int]) -> int:
    if len(nums) < 2:
        return len(nums)

    last_element = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] == last_element:
            nums.pop(i)
        else:
            last_element = nums[i]
            i += 1
    
    return len(nums)

