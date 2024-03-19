from typing import List

def generate(numRows: int) -> List[List[int]]:
    if numRows == 1:
        return [[1]]

    triangle = [[1], [1, 1]]

    for i in range(2, numRows):
        prev_row = triangle[i - 1]

        new_row = [1]

        for j in range(1, len(prev_row)):
            val = prev_row[j - 1] + prev_row[j]
            new_row.append(val)

        new_row.append(1)
        triangle.append(new_row)

    return triangle

