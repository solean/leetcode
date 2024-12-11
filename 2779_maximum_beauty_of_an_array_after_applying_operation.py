from typing import List

def maximumBeauty(nums: List[int], k: int) -> int:
    nums.sort()

    n = len(nums)
    maxlen = 1
    j = 1

    for i in range(n):
        while j < n and nums[j] - nums[i] <= 2 * k:
            j += 1
            maxlen = max(maxlen, j - i)

    return maxlen

