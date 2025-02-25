from typing import List

def findMaxConsecutiveOnes(nums: List[int]) -> int:
    n = len(nums)
    if n < 2:
        return 1

    left_count = nums.copy()
    all_ones = True
    for i in range(1, n):
        if nums[i] > 0:
            left_count[i] = left_count[i - 1] + 1
        else:
            all_ones = False

    if all_ones:
        return n

    right_count = nums.copy()
    for i in range(n - 2, -1, -1):
        if nums[i] > 0:
            right_count[i] = right_count[i + 1] + 1

    max_ones = 0
    for i in range(n):
        if nums[i] == 0:
            num_ones = 0
            if i == 0:
                num_ones = right_count[1] + 1
            elif i == n - 1:
                num_ones = left_count[-2] + 1
            else:
                num_ones = left_count[i - 1] + right_count[i + 1] + 1

            max_ones = max(max_ones, num_ones)

    return max_ones

