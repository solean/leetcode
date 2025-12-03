from typing import List

def maxDistance(arrays: List[List[int]]) -> int:
    res = 0
    min_num = arrays[0][0]
    max_num = arrays[0][-1]

    for i in range(1, len(arrays)):
        arr = arrays[i]

        res = max(res, max(abs(arr[-1] - min_num), abs(max_num - arr[0])))
        min_num = min(min_num, arr[0])
        max_num = max(max_num, arr[-1])

    return res

