from typing import List

def all_paths_source_target(graph: List[List[int]]) -> List[List[int]]:
    paths = []

    def dfs(node, curr_path):
        if node == len(graph) - 1:
            paths.append(curr_path)
            return

        for neighbor in graph[node]:
            new_path = curr_path.copy()
            new_path.append(neighbor)
            dfs(neighbor, new_path)

    dfs(0, [0])
    return paths