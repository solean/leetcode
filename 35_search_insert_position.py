from typing import List

# If target is not present in nums, return the index where it would be if inserted
def search_insert(nums: List[int], target: int) -> int:
    i = 0
    j = len(nums) - 1

    while i < j:
        mid = (i + j) // 2
        if target > nums[mid]:
            i = mid + 1
        elif target < nums[mid]:
            j = mid - 1
        else:
            return mid

    # If this is reached, target was not found
    return i + 1 if target > nums[i] else i

