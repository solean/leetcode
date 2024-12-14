from typing import List
import heapq

def longestSubarray(nums: List[int], limit: int) -> int:
    minheap = []
    maxheap = []
    i, j = 0, 0
    maxlen = 0

    while j < len(nums):
        heapq.heappush(minheap, (nums[j], j))
        heapq.heappush(maxheap, (-nums[j], j))

        while i < j and abs(-maxheap[0][0] - minheap[0][0]) > limit:
            i += 1

            while minheap and minheap[0][1] < i:
                heapq.heappop(minheap)
            while maxheap and maxheap[0][1] < i:
                heapq.heappop(maxheap)

        maxlen = max(maxlen, j - i + 1)

        j += 1

    return maxlen

