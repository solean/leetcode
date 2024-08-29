from typing import List

def countSubIslands(grid1: List[List[int]], grid2: List[List[int]) -> int:
    rows = len(grid1)
    cols = len(grid1[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    num_sub_islands = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid2[r][c] == 0 or (r, c) in visited:
            return True

        visited.add((r, c))

        result = True
        if grid1[r][c] == 0:
            result = False
        for x, y in dirs:
            result = dfs(r + x, c + y) and result

        return result


    for r in range(rows):
        for c in range(cols):
            if grid2[r][c] == 1 and (r, c) not in visited:
                if dfs(r, c):
                    num_sub_islands += 1

    return num_sub_islands

