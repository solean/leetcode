from typing import List
from collections import deque

def closestMeetingNode(edges: List[int], node1: int, node2: int) -> int:

    def bfs(startnode, distances):
        q = deque([(startnode, 0)])
        visited = set()
        while q:
            node, dist = q.popleft()
            visited.add(node)
            distances[node] = dist

            dest = edges[node]
            if dest not in visited and dest > -1:
                q.append((dest, dist + 1))


    n = len(edges)
    distances1 = [-1] * n
    distances2 = [-1] * n

    bfs(node1, distances1)
    bfs(node2, distances2)

    closest_node = -1
    min_seen = float("inf")
    for node in range(n):
        d1, d2 = distances1[node], distances2[node]
        if d1 != -1 and d2 != -1:
            if max(d1, d2) < min_seen:
                min_seen = max(d1, d2)
                closest_node = node

    return closest_node

