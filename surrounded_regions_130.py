from typing import List

def solve(board: List[List[str]]) -> None:
    rows = len(board)
    cols = len(board[0])
    dont_flip = set()
    visited = set()
    dirs =[(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(i, j):
        for dx, dy in dirs:
            x, y = i + dx, j + dy
            if 0 <= x < rows and 0 <= y < cols and (x, y) not in visited and board[i][j] == "O":
                dont_flip.add((x, y))
                visited.add((x, y))
                dfs(x, y)

    for i in range(rows):
        for j in range(cols):
            # Start from the edges of the board and dfs any "O"s
            if (i == 0 or i == rows - 1 or j == 0 or j == cols - 1) and (i, j) not in visited and board[i][j] == "O":
                dont_flip.add((i, j))
                visited.add((i, j))
                dfs(i, j)
    
    for i in range(rows):
        for j in range(rows):
            if (i, j) not in dont_flip:
                board[i][j] = "X"
