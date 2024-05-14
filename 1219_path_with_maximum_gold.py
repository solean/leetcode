from typing import List

def getMaximumGold(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    dirs = ((0, -1), (0, 1), (1, 0), (-1, 0))
    max_gold = 0

    def dfs(x, y, visited):
        if (x, y) in visited or grid[x][y] == 0:
            return 0
        
        visited.add((x, y))
        gold = grid[x][y]
        
        for dx, dy in dirs:
            if 0 <= x + dx < rows and 0 <= y + dy < cols:
                gold = max(gold, grid[x][y] + dfs(x + dx, y + dy, visited))
        visited.remove((x, y))
        
        return gold
    

    for r in range(rows):
        for c in range(cols):
            max_gold = max(max_gold, dfs(r, c, set()))

    return max_gold

