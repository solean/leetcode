from typing import List

def maximumTripletValue(nums: List[int]) -> int:
    n = len(nums)
    max_val = 0

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                curr = (nums[i] - nums[j]) * nums[k]
                max_val = max(max_val, curr)

    return max_val

