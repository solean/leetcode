from typing import List
import math

# O(n) solution
def search_insert_o_n(nums: List[int], target: int) -> int:
    for i in range(0, len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)

# O(log n) solution (binary search)
def search_insert(nums: List[int], target: int) -> int:
    l = 0
    h = len(nums) - 1

    while l <= h:
        mid = math.floor((l + h ) / 2)
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            h = mid - 1
        else:
            return mid

    return l

