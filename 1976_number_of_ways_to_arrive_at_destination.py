from typing import List
from collections import defaultdict
import heapq

def countPaths(n: int, roads: List[List[int]]) -> int:
    adj = defaultdict(list)
    for a, b, weight in roads:
        adj[a].append((b, weight))
        adj[b].append((a, weight))

    min_heap = [(0, 0)]
    min_cost = [float("inf")] * n
    path_count = [0] * n
    path_count[0] = 1
    MOD = 10**9 + 7

    while min_heap:
        cost, node = heapq.heappop(min_heap)

        for nei, nei_cost in adj[node]:
            if cost + nei_cost < min_cost[nei]:
                min_cost[nei] = cost + nei_cost
                path_count[nei] = path_count[node]
                heapq.heappush(min_heap, (cost + nei_cost, nei))
            elif cost + nei_cost == min_cost[nei]:
                path_count[nei] = (path_count[nei] + path_count[node]) % MOD

    return path_count[-1]

