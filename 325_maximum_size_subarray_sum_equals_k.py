from typing import List

def maxSubArrayLen(nums: List[int, k: int]) -> int:
    n = len(nums)
    res = 0

    ps = [0] * n
    ps[0] = nums[0]

    ps_to_index_map = {}
    ps_to_index_map[ps[0]] = 0

    for i in range(n):
        if i == 0:
            ps[i] = nums[i]
        else:
            ps[i] = ps[i - 1] + nums[i]

        if ps[i] == k:
            res = max(res, i + 1)
        elif ps[i] - k in ps_to_index_map:
            res = max(res, i - ps_to_index_map[ps[i] - k])

        if ps[i] not in ps_to_index_map:
            ps_to_index_map[ps[i]] = i

    return res

