from typing import List
from collections import defaultdict

def treeDiameter(edges: List[List[int]]) -> int:
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    def bfs(start):
        q = deque([start])
        visited = set()
        n = 0
        last_node = start

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                last_node = node
                visited.add(node)

                for nei in adj[node]:
                    if nei not in visited:
                        q.append(nei)

            if q:
                n += 1

        return last_node, n


    last_node, _ = bfs(0)
    _, diameter = bfs(last_node)
    return diameter

