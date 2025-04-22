from typing import List
from collections import defaultdict

class Solution:
    def min_reorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append((b, b))
            adj[b].append((a, b))

        res = [0]
        visited = set()

        def dfs(node):
            visited.add(node)

            for nei, endpoint in adj[node]:
                if nei not in visited:
                    if nei == endpoint:
                        res[0] += 1
                    dfs(nei)


        dfs(0)
        return res[0]

