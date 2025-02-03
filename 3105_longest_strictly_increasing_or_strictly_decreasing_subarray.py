from typing import List

def longestMonotonicSubarray(nums: List[int]) -> int:
    n = len(nums)
    longest = 1

    i = 0
    while i < n:
        j = i + 1
        while j < n and nums[j] > nums[j - 1]:
            longest = max(longest, j - i + 1)
            j += 1
        i = j

    i = 0
    while i < n:
        j = i + 1
        while j < n and nums[j] < nums[j - 1]:
            longest = max(longest, j - i + 1)
            j += 1
        i = j

    return longest

