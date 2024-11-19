from typing import List
from collections import deque

def shortestSubarray(nums: List[int], k: int) -> int:
    res = float("inf")
    curr_sum = 0
    q = deque()

    for r in range(len(nums)):
        curr_sum += nums[r]

        if curr_sum >= k:
            res = min(res, r + 1)

        while q and curr_sum - q[0][0] >= k:
            prefix, end_idx = q.popleft()
            res = min(res, r - end_idx)

        while q and q[-1][0] > curr_sum:
            q.pop()

        q.append((curr_sum, r))

    return -1 if res == float("inf") else res

