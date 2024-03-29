from typing import List

def find_ball(grid: List[List[int]]) -> List[int]:
    num_rows = len(grid)
    num_cols = len(grid[0])
    result = [None for i in range(num_cols)]

    for col in range(num_cols):
        curr = col

        for row in range(num_rows):
            next_col = curr + grid[row][curr]

            # check if ball is trapped
            if next_col < 0 or next_col > num_cols - 1 or grid[row][curr] != grid[row][next_col]:
                result[col] = -1
                break

            result[col] = next_col
            curr = next_col

    return result
