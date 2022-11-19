from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    for row in matrix:
        if row[0] <= target <= row[-1]:
            l = 0
            r = len(row) - 1
            while l <= r:
                mid = (l + r) // 2
                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

            break

    return False
