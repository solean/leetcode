from typing import List

def countBattleships(board: List[List[str]]) -> int:
    rows, cols = len(board), len(board[0])
    num_ships = 0
    visited = set()

    def dfs(r, c):
        visited.add((r, c))

        # go left
        i = c
        while i >= 0 and board[r][i] == "X":
            visited.add((r, i))
            i -= 1
        # go right
        i = c
        while i < cols and board[r][i] == "X":
            visited.add((r, i))
            i += 1
        # go up
        i = r
        while i >= 0 and board[i][c] == "X":
            visited.add((i, c))
            i -= 1
        # go down
        i = r
        while i < rows and board[i][c] == "X":
            visited.add((i, c))
            i += 1

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "X" and (r, c) not in visited:
                num_ships += 1
                dfs(r, c)

    return num_ships

