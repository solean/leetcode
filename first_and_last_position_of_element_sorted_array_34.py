from typing import List
import math
from misc import binary_search

def search_range(nums: List[int], target: int) -> List[int]:
    if len(nums) == 0:
        return [-1, -1]
    elif len(nums) == 1:
        if nums[0] == target:
            return [0, 0]
        else:
            return [-1, -1]

    match_index = binary_search(nums, target)
    low_index = match_index
    high_index = match_index

    if match_index < 0:
        return [-1, -1]

    i = low_index
    while i >= 0:
        if nums[i] == target:
            low_index = i
        i -= 1

    j = high_index
    while j < len(nums):
        if nums[j] == target:
            high_index = j
        j += 1

    return [low_index, high_index]

