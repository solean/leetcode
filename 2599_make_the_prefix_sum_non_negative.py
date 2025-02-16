from typing import List
import heapq

def makePrefSumNonNegative(nums: List[int]) -> int:
    res = 0
    ps = 0
    min_heap = []

    for n in nums:
        if n < 0:
            heapq.heappush(min_heap, n)

        ps += n
        if ps < 0:
            min_seen = heapq.heappop(min_heap)
            ps -= min_seen
            res += 1

    return res

