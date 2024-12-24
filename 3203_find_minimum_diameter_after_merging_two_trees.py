import math
from typing import List
from collections import defaultdict

def minimumDiameterAfterMerge(edges1: List[List[int]], edges2: List[List[int]]) -> int:
    adj1 = defaultdict(list)
    for a, b in edges1:
        adj1[a].append(b)
        adj1[b].append(a)
    adj2 = defaultdict(list)
    for a, b in edges2:
        adj2[a].append(b)
        adj2[b].append(a)

    def bfs(start, adj):
        q = deque()
        q.append(start)
        n = 0
        last_node = start
        visited = set()

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

    def find_diameter(adj):
        last_node, _ = bfs(0, adj)
        _, diameter = bfs(last_node, adj)
        return diameter

    d1 = find_diameter(adj1)
    d2 = find_diameter(adj2)

    combined = math.ceil(d1 / 2) + math.ceil(d2 / 2) + 1

    return max(d1, d2, combined)

