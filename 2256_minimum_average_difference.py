from typing import List

def minimumAverageDifference(nums: List[int]) -> int:
    if len(nums) < 2:
        return 0

    left_sum = 0
    right_sum = sum(nums)
    min_diff = float('inf')
    min_i = None

    for i in range(len(nums)):
        left_sum += nums[i]
        right_sum -= nums[i]

        if len(nums) - 1 - i > 0:
            diff = (left_sum // (i + 1)) - (right_sum // (len(nums) - 1 - i))
        else:
            diff = left_sum // (i + 1)

        diff = abs(diff)
        print(i, diff)
        if diff < min_diff:
            min_diff = diff
            min_i = i

    return min_i