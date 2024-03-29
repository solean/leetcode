from typing import List

def combine(n: int, k: int) -> List[List[int]]:
    combos = []

    def dfs(i, path):
        if i not in path:
            path.append(i)

        if len(path) == k:
            combos.append(path.copy())
            return

        for j in range(i + 1, n + 1):
            dfs(j, path.copy())


    for i in range(1, n + 1):
        dfs(i, [])

    return combos