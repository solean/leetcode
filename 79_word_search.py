from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    num_rows = len(board)
    num_cols = len(board[0])

    def dfs(r, c, i):
        if i == len(word):
            return True

        if (r < 0 or c < 0 or r >= len(num_rows) or c >= len(num_cols)
                or board[r][c] != word[i] or board[r][c] == 0):
            return False

        temp = board[r][c]
        board[r][c] = 0

        i += 1
        result = (dfs(r, c + 1, i) or
                  dfs(r, c - 1, i) or
                  dfs(r + 1, c, i) or
                  dfs(r - 1, c, i))

        board[r][c] = temp

        return result

    for r in range(num_rows):
        for c in range(num_cols):
            if dfs(r, c, 0):
                return True

    return False