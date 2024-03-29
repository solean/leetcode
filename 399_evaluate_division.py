from typing import List
from collections import defaultdict, deque

def calcEquation(equations: List[List[int]], values: List[float], queries: List[List[int]]) -> List[float]:
    adj = defaultdict(list)
    for i in range(len(equations)):
        adj[a].append((b, values[i]))
        adj[b].append((a, 1 / values[i]))


    def bfs(src, target):
        if src not in adj or target not in adj:
            return -1

        q = deque()
        q.append((src, 1))
        visited = set()
        visited.add(src)

        while q:
            node, weight = q.popleft()

            if node == target:
                return weight

            for nei, nei_weight in adj[node]:
                if nei not in visited:
                    q.append((nei, nei_weight * weight))
                    visited.add(nei)

        return -1


    answers = []
    for query in queries:
        answers.append(bfs(query[0], query[1]))
    return answers

