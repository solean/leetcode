from typing import List
from collections import defaultdict, deque

def valid_path(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    adj = defaultdict(list)

    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])

    q = deque()
    q.append(source)
    visited = set()

    while q:
        node = q.popleft()

        if node == destination:
            return True

        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

    return False