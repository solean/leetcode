from typing import List

# Using O(m + n) space
def set_zeroes_with_space(matrix: List[List[int]]) -> None:
    m = len(matrix)
    n = len(matrix[0])
    rows = set()
    cols = set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for i in range(m):
        for j in range(n):
            if i in rows or j in cols:
                matrix[i][j] = 0


# Using O(1) extra space
def set_zeroes_with_no_extra_space(matrix: List[List[int]]) -> None:
    m = len(matrix)
    n = len(matrix[0])

    should_zero_first_row = any(matrix[0][j] == 0 for j in range(n))
    should_zero_first_col = any(matrix[i][0] == 0 for i in range(m))

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if should_zero_first_row:
        for j in range(n):
            matrix[0][j] = 0

    if should_zero_first_col:
        for i in range(m):
            matrix[i][0] = 0

