from typing import List
import heapq

def minOperations(nums: List[int], k: int) -> int:
    heapq.heapify(nums)
    res = 0

    while nums and nums[0] < k:
        res += 1
        x, y = heapq.heappop(nums), heapq.heappop(nums)
        newnum = min(x, y) * 2 + max(x, y)
        heapq.heappush(nums, newnum)

    return res

