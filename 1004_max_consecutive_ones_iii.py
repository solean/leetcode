from typing import List

def longestOnes(nums: List[int], k: int) -> int:
    max_window = 0
    l, r = 0, 0
    num_zeros = 0

    while r < len(nums):
        if nums[r] == 0:
            num_zeros += 1

        while num_zeros > k:
            if nums[l] == 0:
                num_zeros -= 1
            l += 1

        r += 1
        max_window = max(max_window, r - l)

    return max_window

