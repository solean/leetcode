from typing import List
import heapq

def find_kth_largest(nums: List[int], k: int) -> int:
    nums = list(map(lambda n: n * -1, nums))
    heapq.heapify(nums)

    for _ in range(k - 1):
        heapq.heappop(nums)

    return heapq.heappop(nums) * -1