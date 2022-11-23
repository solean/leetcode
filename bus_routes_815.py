from typing import List
from collections import defaultdict, deque

def num_buses_to_destination(routes: List[List[int]], source: int, target: int) -> int:

    stop_to_route = defaultdict(set)
    for i, route in enumerate(routes):
        for j in range(len(route)):
            stop_to_route[route[j]].add(i)

    q = deque()
    q.append([source, 0])
    visited = set()
    visited.add(source)
    
    while q:
        stop, bus = q.popleft()

        if stop == target:
            return bus
        
        for route in stop_to_route[stop]:
            for next_stop in routes[route]:
                if next_stop not in visited:
                    q.append([next_stop, bus + 1])
                    visited.add(next_stop)

            routes[route] = []

    return -1