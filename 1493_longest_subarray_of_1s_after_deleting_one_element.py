from typing import List

def longestSubarray(nums: List[int]) -> int:
    l = 0
    longest = 0
    num_zeros = 0

    for r in range(len(nums)):
        if nums[r] == 0:
            num_zeros += 1

        while num_zeros > 1:
            if nums[l] == 0:
                num_zeros -= 1
            l += 1

        longest = max(longest, r - l)

    return longest

