from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows - 2):
            for c in range(cols - 2):
                if self.is_magic_square(grid, r, c):
                    res += 1

        return res

    def is_magic_square(self, grid, r, c):
        seen = [False] * 10

        for i in range(3):
            for j in range(3):
                n = grid[r + i][c + j]
                if n < 1 or n > 9:
                    return False
                if seen[n]:
                    return False
                seen[n] = True

        # check diagonal sums
        diag1 = grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2]
        diag2 = grid[r + 2][c] + grid[r + 1][c + 1] + grid[r][c + 2]

        if diag1 != diag2:
            return False

        # check row sums
        row1 = grid[r][c] + grid[r][c + 1] + grid[r][c + 2]
        row2 = grid[r + 1][c] + grid[r + 1][c + 1] + grid[r + 1][c + 2]
        row3 = grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2]

        if not (row1 == diag1 and row2 == diag1 and row3 == diag1):
            return False

        # check column sums
        col1 = grid[r][c] + grid[r + 1][c] + grid[r + 2][c]
        col2 = grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 2][c + 1]
        col3 = grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2]

        if not (col1 == diag1 and col2 == diag1 and col3 == diag1):
            return False

        return True

