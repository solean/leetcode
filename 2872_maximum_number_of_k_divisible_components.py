from typing import List
from collections import defaultdict

def maxKDivisibleComponents(n: int, edges: List[List[int]], values: List[int], k: int) -> int:
    res = 0

    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    def dfs(node, parent):
        nonlocal res

        sm = 0

        for nei in adj[node]:
            if nei != parent:
                sm += dfs(nei, node)

        sm += values[node]
        if sm % k == 0:
            res += 1

        return sm

    dfs(0, None)
    return res

