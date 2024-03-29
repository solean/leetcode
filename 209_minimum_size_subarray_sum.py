from typing import List

def minimum_size_subarray_sum(target: int, nums: List[int]) -> int:
    l = 0
    min_length = len(nums)
    curr_sum = 0
    found = False

    for r in range(len(nums)):
        curr_sum += nums[r]

        while curr_sum >= target:
            found = True
            min_length = min(min_length, r - l + 1)
            curr_sum -= nums[l]
            l += 1


    return min_length if found else 0
