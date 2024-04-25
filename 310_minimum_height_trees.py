from typing import List 
from collections import deque

def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    if n == 1:
        return [0]

    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    
    edge_count = {}
    leaves = deque()

    for node, neighbors in adj.items():
        if len(neighbors) == 1:
            leaves.append(node)
        edge_count[node] = len(neighbors)
    
    while leaves:
        if n <= 2:
            return list(leaves)

        for i in range(len(leaves)):
            node = leaves.popleft()
            n -= 1

            for neighbor in adj[node]:
                edge_count[neighbor] -= 1
                if edge_count[neighbor] == 1:
                    leaves.append(neighbor)
