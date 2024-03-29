from typing import List
from collections import Counter, defaultdict

def count_sub_trees(n: int, edges: List[List[int]], labels: str) -> List[int]:
    output = [0] * n
    adj = defaultdict(list)
    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])

    def dfs(node, parent):
        counts = Counter()
        for neighbor in adj[node]:
            if neighbor != parent:
                counts += dfs(neighbor, node)

        counts[labels[node]] += 1
        output[node] = counts[labels[node]]

        return counts

    dfs(0, -1)
    return output