from typing import List
import heapq

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    if len(nums) <= 1:
        return nums

    maxheap = []
    for i in range(k):
        heapq.heappush(maxheap, (-nums[i], i))

    res = [-maxheap[0][0]]

    i = 1
    j = k

    while j < len(nums):
        heapq.heappush(maxheap, (-nums[j], j))
        while maxheap[0][1] < i:
            heapq.heappop(maxheap)

        res.append(-maxheap[0][0])

        i += 1
        j += 1

    return res

