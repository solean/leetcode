from typing import List

def canSortArrayON2(nums: List[int]) -> bool:
    n = len(nums)
    values = nums.copy()

    for i in range(n):
        for j in range(n - i - 1):
            if values[j] <= values[j + 1]:
                continue

            if bin(values[j]).count("1") == bin(values[j + 1]).count("1"):
                values[j], values[j + 1] = values[j + 1], values[j]
            else:
                return False

    return True

