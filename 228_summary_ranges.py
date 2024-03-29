from typing import List

def summaryRanges(nums: List[int]) -> List[str]:
    ranges = []
    i, j = 0, 0

    while i < len(nums):
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        
        if i == j:
            ranges.append(f"{nums[i]}")
        else:
            ranges.append(f"{nums[i]}->{nums[j]}")
        
        j += 1
        i = j
    
    return ranges
