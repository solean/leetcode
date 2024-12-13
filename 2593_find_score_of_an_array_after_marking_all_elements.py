from typing import List
import heapq

def findScore(nums: List[int]) -> int:
    n = len(nums)
    # (value, index)
    minheap = []
    marked = [False] * n
    score = 0

    for i in range(n):
        heapq.heappush(minheap, (nums[i], i))

    while minheap:
        val, i = heapq.heappop(minheap)
        if marked[i]:
            continue
        else:
            score += val

        marked[i] = True
        if i > 0:
            marked[i - 1] = True
        if i < n - 1:
            marked[i + 1] = True

    return score

