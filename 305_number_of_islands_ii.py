from typing import List
from misc import UnionFind

def numIslands2(m: int, n: int, positions: List[List[int]]) -> List[int]:
    grid = [[0] * n for _ in range(m)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    res = []
    reps = set()
    uf = UnionFind(m * n)

    for r, c in positions:
        grid[r][c] = 1
        reps_to_check = set()

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                reps_to_check.add(uf.find(nr * n + nc))
                uf.union(r * n + c, nr * n + nc)

        reps.add(uf.find(r * n + c))

        for item in reps_to_check:
            reps.remove(item)

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                reps.add(uf.find(nr * n + nc))

        res.append(len(reps))

    return res

