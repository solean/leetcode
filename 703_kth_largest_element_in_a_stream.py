from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        if len(self.heap) > self.k - 1:
            # heappushpop is more efficient than calling heappush and heappop separately
            heapq.heappushpop(self.heap, val)
        else:
            heapq.heappush(self.heap, val)

        return self.heap[0]