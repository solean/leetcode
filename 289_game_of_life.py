from typing import List

# Solution using O(m + n) extra space
def game_of_life_with_extra_space(board: List[List[int]]) -> None:
    rows = len(board)
    cols = len(board[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    new_grid = [[0 for col in range(cols)] for row in range(rows)]

    for r in range(rows):
        for c in range(cols):
            live = board[r][c] == 1
            live_neighbors = 0

            for dr, dc in dirs:
                x, y = r + dr, c + dc
                if 0 <= x < rows and 0 <= y < cols and board[x][y] == 1:
                    live_neighbors += 1

            if (live and (live_neighbors == 2 or live_neighbors == 3)) or (not live and live_neighbors == 3):
                new_grid[r][c] = 1

    for r in range(rows):
        for c in range(cols):
            board[r][c] = new_grid[r][c]


# In-place solution using O(1) extra space
def game_of_life_no_extra_space(board: List[List[int]]) -> None:
    rows = len(board)
    cols = len(board[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
 
    for r in range(rows):
        for c in range(cols):
            live = board[r][c] == 1
            live_neighbors = 0

            for dr, dc in dirs:
                x, y = r + dr, c + dc
                if 0 <= x < rows and 0 <= y < cols and board[x][y] in (1, 3):
                    live_neighbors += 1

            if live and live_neighbors in (2, 3):
                board[r][c] = 3
            elif not live and live_neighbors == 3:
                board[r][c] = 2

    for r in range(rows):
        for c in range(cols):
            if board[r][c] in (2, 3):
                board[r][c] = 1
            else:
                board[r][c] = 0

