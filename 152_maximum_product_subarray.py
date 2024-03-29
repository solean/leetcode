from typing import List

def max_product(nums: List[int]) -> int:
    curr_max = nums[0]
    curr_min = nums[0]
    global_max = nums[0]

    for i in range(1, len(nums)):
        n = nums[i]

        temp_max = curr_max
        curr_max = max(n, n * curr_max, n * curr_min)
        curr_min = min(n, n * temp_max, n * curr_min)

        global_max = max(global_max, curr_max)

    return global_max