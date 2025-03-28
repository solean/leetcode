from typing import List
from collections import defaultdict
import heapq

def minimumDistance(n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
    adj = defaultdict(list)
    for a, b, weight in edges:
        adj[a].append((b, weight))

    marked_set = set(marked)
    distances = [float("inf")] * n
    distances[s] = 0
    visited = [False] * n

    min_heap = []
    for i, d in enumerate(distances):
        heapq.heappush(min_heap, (d, i))

    min_distance_to_marked = float("inf")

    while min_heap:
        distance, node = heapq.heappop(min_heap)

        if visited[node] or distance > distances[node]:
            continue
        visited[node] = True

        for nei, weight in adj[node]:
            if distance + weight < distances[nei]:
                distances[nei] = distance + weight
                heapq.heappush(min_heap, (distance + weight, nei))

                if nei in marked:
                    min_distance_to_marked = min(min_distance_to_marked, distances[nei])

    return min_distance_to_marked if min_distance_to_marked < float("inf") else -1

