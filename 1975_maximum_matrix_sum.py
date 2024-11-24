from typing import List

def maxMatrixSum(matrix: List[List[int]]) -> int:
    num_neg = 0
    abs_sum = 0
    min_abs = float("inf")

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] < 0:
                num_neg += 1
            abs_sum += abs(matrix[i][j])
            min_abs = min(min_abs, abs(matrix[i][j]))

    if num_neg % 2 != 0:
        abs_sum -= (2 * min_abs)

    return abs_sum

