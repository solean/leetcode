from typing import List

def longestNiceSubarray(nums: List[int]) -> int:
    used_bits = 0
    max_len = 0
    i = 0

    for j in range(len(nums)):
        while used_bits & nums[j] != 0:
            used_bits ^= nums[i]
            i += 1

        used_bits |= nums[j]

        max_len = max(max_len, j - i + 1)

    return max_len

