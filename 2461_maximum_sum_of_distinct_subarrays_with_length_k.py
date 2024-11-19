from typing import List
from collections import Counter

def maximumSubarraySum(nums: List[int], k: int) -> int:
    in_window = Counter(nums[:k])
    curr_sum = sum(nums[:k])
    max_sum = curr_sum if len(in_window) == k else 0
    i = 1
    j = k

    while j < len(nums):
        prev = nums[i - 1]
        next = nums[j]

        in_window[next] += 1
        in_window[prev] -= 1
        if not in_window[prev]:
            del in_window[prev]

        curr_sum -= prev
        curr_sum += next

        if len(in_window) == k:
            max_sum = max(max_sum, curr_sum)

        i += 1
        j += 1

    return max_sum

