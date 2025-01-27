from typing import List
from collections import defaultdict, deque

def checkIfPrerequisite(numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    adj = defaultdict(list)
    for a, b in prerequisites:
        adj[a].append(b)

    can_take = [[False] * numCourses for _ in range(numCourses)]

    def bfs(start):
        q = deque([start])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                can_take[start][node] = True

                for nei in adj[node]:
                    if not can_take[start][nei]:
                        q.append(nei)

    for i in range(numCourses):
        bfs(i)

    return [can_take[qa][qb] for qa, qb in queries]

