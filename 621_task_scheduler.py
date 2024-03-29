from typing import List
from collections import deque
import heapq

def least_interval(tasks: List[str], n: int) -> int:
    counts = {}
    for t in tasks:
        if t in counts:
            counts[t] += 1
        else:
            counts = 1

    heap = [-c for c in counts.values()]
    heapq.heapify(heap)

    time = 0
    q = deque()

    while heap or q:
        time += 1

        if heap:
            count = heapq.heappop(heap)
            count += 1
            if count:
                q.append([count, time + n])
        
        if q and q[0][1] == time:
            heapq.heappush(heap, q.popleft()[0])

    return time