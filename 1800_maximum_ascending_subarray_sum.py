from typing import List

def maxAscendingSum(nums: List[int]) -> int:
    n = len(nums)
    max_sum = 0

    i = 0
    while i < n:
        curr_sum = nums[i]

        j = i + 1
        while j < n and nums[j] > nums[j - 1]:
            curr_sum += nums[j]
            j += 1

        max_sum = max(max_sum, curr_sum)
        i = j

    return max_sum

