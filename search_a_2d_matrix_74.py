from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    low = 0
    high = len(matrix) - 1

    while low <= high:
        mid = (low + high) // 2

        if target < matrix[mid][0]:
            high = mid - 1
        else:
            row = matrix[mid]
            if target > row[len(row) - 1]:
                low = mid + 1
            else: # if target is in the matrix, it will be in this row
                rowLow = 0
                rowHigh = len(row) - 1

                while rowLow <= rowHigh:
                    rowMid = (rowLow + rowHigh) // 2

                    if target == row[rowMid]:
                        return True
                    elif target > row[rowMid]:
                        rowLow = rowMid + 1
                    else:
                        rowHigh = rowMid - 1

                return False

    return False