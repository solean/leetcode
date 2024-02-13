from typing import List

def max_subarray_sum_circular(nums: List[int]) -> int:
    mx = nums[0]
    local_max = nums[0]
    mn = nums[0]
    local_min = nums[0]
    total = nums[0]

    for i in range(1, len(nums)):
        n = nums[i]
        total += n

        local_max = max(n, n + local_max)
        mx = max(mx, local_max)

        local_min = min(n, n + local_min)
        mn = min(mn, local_min)

    if mx < 0:
        return mx
    else:
        return max(mx, total - mn)

