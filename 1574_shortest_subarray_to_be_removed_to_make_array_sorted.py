from typing import List

def findLengthOfShortestSubarray(arr: List[int]) -> int:
    n = len(arr)

    # Find longest sorted prefix
    i = 0
    while i < n - 1 and arr[i + 1] >= arr[i]:
        i += 1

    if i == n - 1:
        # check for already sorted array
        return 0

    # Find longest sorted suffix
    j = n - 1
    while j > 0 and arr[j - 1] <= arr[j]:
        j -= 1

    result = min(n - (i + 1), j)

    # Try to merge prefix with suffix (i = end of prefix, j = start of suffix)
    l = 0
    r = j
    while l <= i and r < n:
        if arr[l] <= arr[r]:
            result = min(result, r - l - 1)
            l += 1
        else:
            r += 1

    return result

