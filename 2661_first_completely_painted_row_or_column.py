from typing import List
from collections import defaultdict

def firstCompleteIndex(arr: List[int], matrix: List[List[int]]) -> int:
    rows, cols = len(matrix), len(matrix[0])
    row_counts = defaultdict(int)
    col_counts = defaultdict(int)
    locations = {}

    for r in range(rows):
        for c in range(cols):
            locations[matrix[r][c]] = (r, c)

    for i, n in enumerate(arr):
        r, c = locations[n]

        row_counts[r] += 1
        if row_counts[r] == cols:
            return i

        col_counts[c] += 1
        if col_counts[c] == rows:
            return i

    return -1

