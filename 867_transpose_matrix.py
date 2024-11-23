from typing import List

def transpose(matrix: List[List[int]]) -> List[List[int]]:
    rows = len(matrix)
    cols = len(matrix[0])
    res = [[0 for _ in range(rows)] for _ in range(cols)]

    for r in range(cols):
        for c in range(rows):
            res[r][c] = matrix[c][r]

    return res

