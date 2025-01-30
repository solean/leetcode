from typing import List

def isBipartite(graph: List[List[int]]) -> bool:
    color = {}

    def bfs(start):
        color[start] = 1
        q = deque([start])
        while q:
            node = q.popleft()
            for nei in graph[node]:
                if nei in color:
                    if color[nei] == color[node]:
                        return False
                    else:
                        continue
                else:
                    color[nei] = -color[node]
                    q.append(nei)
        return True

    for i in range(len(graph)):
        if i not in color:
            if not bfs(i):
                return False

    return True

