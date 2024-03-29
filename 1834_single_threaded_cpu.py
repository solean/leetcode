from typing import List
from collections import defaultdict
import heapq

def get_order(tasks: List[List[int]]) -> List[int]:
    order = []
    available = []

    # (start time, processing time, original index)
    tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])

    time = 1
    i = 0
    while len(order) != len(tasks):
        while i < len(tasks) and tasks[i][0] <= time:
            heapq.heappush(available, tasks[i])
            i += 1

        if available:
            next_task = heapq.heappop(available)
            time += next_task[0]
            order.append(next_task[2])
        else:
            time = tasks[i][0]

    return order