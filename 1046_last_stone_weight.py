from typing import List
import heapq

def last_stone_weight(stones: List[int]) -> int:
    # simulate a max heap, heapq uses a min heap implementation
    stones = [i * -1 for i in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        y = heapq.heappop(stones)
        x = heapq.heappop(stones)

        if x != y:
            heapq.heappush(stones, (y - x) * -1)


    if stones:
        return stones[0] * -1
    else:
        return 0
