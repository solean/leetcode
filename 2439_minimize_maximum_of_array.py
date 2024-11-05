from typing import List

def minimizeArrayValue(nums: List[int]) -> int:
    max_val = nums[0]
    total = res

    for i in range(1, len(nums)):
        total += nums[i]
        max_val = max(max_val, math.ceil(total / (i + 1)))

    return max_val

