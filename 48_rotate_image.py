from typing import List

# modify matrix in-place
def rotate(matrix: List[List[int]]) -> None:
    l = len(matrix)
    for i in range(l // 2):
        for j in range(i, l - i - 1):
            # store top left value
            temp = matrix[i][j]
            # top left = bottom left
            matrix[i][j] = matrix[l - 1 - j][i]
            # bottom left = bottom right
            matrix[l - 1 - j][i] = matrix[l - 1 - i][l - 1 - j]
            # bottom right = top right
            matrix[l - 1 - i][l - 1 - j] = matrix[j][l - 1 - i]
            # top right = top left
            matrix[j][l - 1 - i] = temp

