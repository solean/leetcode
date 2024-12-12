from typing import List
import heapq

def pickGifts(gifts: List[int], k: int) -> int:
    max_heap = [-1 * item for item in gifts]
    heapq.heapify(max_heap)

    for _ in range(k):
        big_pile = -1 * heapq.heappop(max_heap)
        new_pile = math.floor(math.sqrt(big_pile))
        heapq.heappush(max_heap, -1 * new_pile)

    gifts_left = [-1 * item for item in max_heap]
    return sum(gifts_left)

