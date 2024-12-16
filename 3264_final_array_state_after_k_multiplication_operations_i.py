from typing import List
import heapq

def getFinalState(nums: List[int], k: int, multiplier: int) -> List[int]:
    min_heap = [(n, i) for i, n in enumerate(nums)]
    heapq.heapify(min_heap)

    for i in range(k):
        n, index = heapq.heappop(min_heap)
        nums[index] *= multiplier
        heapq.heappush(min_heap, (n * multiplier, index))

    return nums

