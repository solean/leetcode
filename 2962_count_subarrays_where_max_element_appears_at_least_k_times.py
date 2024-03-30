from typing import List

def countSubarrays(nums: List[int], k: int) -> int:
    max_el = max(nums)
    max_count = 0
    i = 0
    count = 0
    
    for j in range(len(nums)):
        if nums[j] == max_el:
            max_count += 1

        while max_count > k or (i <= j and max_count == k and nums[i] != max_el):
            if nums[i] == max_el:
                max_count -= 1
            i += 1
        
        if max_count == k:
            count += i + 1

    return count
