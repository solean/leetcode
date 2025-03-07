from typing import List
import heapq

def totalCost(costs: List[int], k: int, candidates: int) -> int:
    n = len(costs)
    min_heap = []
    l, r = candidates - 1, n - candidates
    for i in range(candidates):
        heapq.heappush(min_heap, (costs[i], i))
        if n - i - 1 > l:
            heapq.heappush(min_heap, (costs[n - i - 1], n - i - 1))

    curr_cost = 0
    for _ in range(k):
        cost, i = heapq.heappop(min_heap)
        curr_cost += cost

        if i <= l:
            l += 1
            if l < r:
                heapq.heappush(min_heap, (costs[l], l))
        else:
            r -= 1
            if l < r:
                heapq.heappush(min_heap, (costs[r], r))

    return curr_cost

