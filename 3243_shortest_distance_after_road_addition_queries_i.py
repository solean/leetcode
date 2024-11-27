from typing import List
from collections import defaultdict, deque

def shortestDistanceAfterQueries(n: int, queries: List[List[int]]) -> List[int]:
    adj = defaultdict(list)
    for i in range(n - 1):
        adj[i].append(i + 1)

    ans = []

    for q in queries:
        adj[q[0]].append(q[1])
        shortest_path = n
        q = deque()
        q.append((0, 0))
        visited = set()

        while q:
            for _ in range(len(q)):
                node, pathlen = q.popleft()
                visited.add(node)
                if node == n - 1:
                    shortest_path = min(shortest_path, pathlen)
                else:
                    for nei in adj[node]:
                        if nei not in visited:
                            q.append((nei, pathlen + 1))

        ans.append(shortest_path)

    return ans

