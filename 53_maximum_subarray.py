from typing import List

# Too slow - O(n^2)
def max_subarray_slow(nums: List[int]) -> int:
    if nums is None or len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]

    max_sum = None

    for i in range(len(nums)):
        for j in range(len(nums), i, -1):
            print(nums[i:j])
            sub_sum = sum(nums[i:j])
            print(sub_sum)
            if max_sum is None or sub_sum > max_sum:
                max_sum = sub_sum

    return max_sum


# Kadane's Algorithm
def max_subarray(nums: List[int]) -> int:
    if nums is None or len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]

    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]

    return max(nums)

