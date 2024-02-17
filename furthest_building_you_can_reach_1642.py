import heapq
from typing import List

def furthest_building(heights: List[int], bricks: int, ladders: int) -> int:
    maxheap = []

    for i in range(len(heights) - 1):
        diff = heights[i + 1] - heights[i]
        if diff <= 0:
            continue
        
        bricks -= diff
        heapq.heappush(maxheap, -diff)

        if bricks < 0:
            if not ladders:
                return i

            ladders -= 1
            bricks += -heapq.heappop(maxheap)

    return len(heights) - 1

