from typing import List

def findFarmland(land: List[List[int]]) -> List[List[int]]:
    rows, cols = len(land), len(land[0])
    visited = set()
    farms = []

    def dfs(x, y):
        farm = [x, y]

        # find bottom boundary
        i = x
        while i + 1 < rows and land[i + 1][y] == 1:
            i += 1

        # find right boundary
        j = y
        while j + 1 < cols and land[x][j + 1] == 1:
            j += 1

        # mark all cells in the rectangle farm as visited
        for r in range(x, i + 1):
            for c in range(y, j + 1):
                visited.add((r, c))

        farm.extend([i, j])
        farms.append(farm)


    for r in range(rows):
        for c in range(cols):
            if land[r][c] == 1 and (r, c) not in visited:
                dfs(r, c)

    return farms

