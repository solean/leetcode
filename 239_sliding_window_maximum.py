from typing import List
from collections import deque
import heapq


def maxSlidingWindowOptimal(nums: List[int], k: int) -> List[int]:
    if len(nums) <= 1:
        return nums

    mq = deque()
    for i in range(k):
        while mq and nums[i] >= mq[-1][0]:
            mq.pop()
        mq.append((nums[i], i))

    res = [mq[0][0]]

    i = 1
    j = k

    while j < len(nums):
        if mq and mq[0][1] <= j - k:
            mq.popleft()

        while mq and nums[j] >= mq[-1][0]:
            mq.pop()

        mq.append((nums[j], j))
        res.append(mq[0][0])

    return res


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

