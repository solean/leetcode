from collections import defaultdict
from typing import List

def find_provinces(isConnected: List[List[int]]) -> int:
    l = len(isConnected)
    visited = set()
    num_provinces = 0

    neighbors = defaultdict(list)
    for i in range(l):
        for j in range(l):
            if isConnected[i][j]:
                neighbors[i].append(j)

    def dfs(n):
        if n in visited:
            return
        visited.add(n)
        for neighbor in neighbors[n]:
            dfs(neighbor)

    for city in range(l):
        if city not in visited:
            dfs(city)
            num_provinces += 1

    return num_provinces