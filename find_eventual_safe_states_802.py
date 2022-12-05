from typing import List

def eventual_safe_nodes(graph: List[List[int]]) -> List[int]:
    safe = []
    computed = {}

    def dfs(node, path):
        if node in path:
            return False
        if node in computed:
            return computed[node]
        
        path.add(node)

        for neighbor in graph[node]:
            if not dfs(neighbor, path):
                computed[node] = False
                return False
            else:
                computed[node] = True
        
        path.remove(node)
        computed[node] = True
        return True


    for i in range(len(graph)):
        if dfs(i, set()):
            safe.append(i)
    
    return safe