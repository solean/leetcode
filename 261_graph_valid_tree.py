from typing import List
from collections import defaultdict

def validTree(n: int, edges: List[List[int]]) -> bool:
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    visited = [False] * n

    def dfs_detect_cycle(node, parent):
        visited[node] = True

        for nei in adj[node]:
            if not visited[nei]:
                if dfs_detect_cycle(nei, node):
                    return True
            elif nei != parent:
                return True

        return False

    num_components = 0

    for i in range(n):
        if not visited[i]:
            if dfs_detect_cycle(i, None):
                return False
            num_components += 1

    if num_components > 1:
        return False

    return True

