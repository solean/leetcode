from typing import List
import heapq

def min_stone_sum(piles: List[int], k: int) -> int:
    max_heap = [-x for x in piles]
    heapq.heapify(max_heap)

    for _ in range(k):
        pile = -heapq.heappop(max_heap)
        pile = pile - (pile // 2)
        heapq.heappush(max_heap, -pile)

    return -sum(max_heap)