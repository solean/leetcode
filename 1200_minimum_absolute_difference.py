from typing import List

def minimumAbsDifference(arr: List[int]) -> List[List[int]]:
    res = []
    arr.sort()

    mindiff = abs(arr[1] - arr[0])

    for i in range(1, len(arr)):
        mindiff = min(mindiff, abs(arr[i] - arr[i - 1]))

    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i - 1]) == mindiff:
            res.append([arr[i - 1], arr[i]])

    return res

