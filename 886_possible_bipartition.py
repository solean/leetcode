from typing import List
from collections import defaultdict

def possible_bipartition(n: int, dislikes: List[List[int]]) -> bool:
    graph = defaultdict(list)
    for edge in dislikes:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # -1 = not visited, 0 = red, 1 = blue
    node_colors = [-1] * (n + 1)

    def dfs(node, color):
        node_colors[node] = color

        for neighbor in graph[node]:
            if node_colors[neighbor] == color:
                return False

            # if not visited, recursive call on the neighbor with opposite color
            if node_colors[neighbor] == -1:
                if not dfs(neighbor, 1 - color):
                    return False

        return True


    for i in range(1, n + 1):
        if node_colors[i] == -1:
            if not dfs(i, 0):
                return False

    return True