from typing import List
import heapq

def maxTwoEvents(events: List[List[int]]) -> int:
    events.sort(key=lambda x: x[0])

    # store (end time, value)
    minheap = []

    max_val, max_sum = 0, 0

    for event in events:
        curr_start, curr_end, curr_val = event
        while minheap and minheap[0][0] < curr_start:
            max_val = max(max_val, minheap[0][1])
            heapq.heappop(minheap)

        max_sum = max(max_sum, max_val + curr_val)
        heapq.heappush(minheap, (curr_end, curr_val))

    return max_sum

