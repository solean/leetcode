from typing import List

def isArraySpecial(nums: List[int], queries: List[List[int]]) -> List[bool]:
    n = len(nums)

    validity = [0] * n
    for i in range(n - 1):
        validity[i] = 1 if (nums[i] % 2) != (nums[i + 1] % 2) else 0

    prefix_sum = [0] * n
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + validity[i - 1]

    res = []
    for start, end in queries:
        valid = True
        if start != end and prefix_sum[end] - prefix_sum[start] != end - start:
            valid = False
        res.append(valid)

    return res

