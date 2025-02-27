from typing import List

def lenLongestFibSubseq(arr: List[int]) -> int:
    res = 0
    indexes = { num: i for i, num in enumerate(arr) }
    dp = {}

    for i in range(len(arr)):
        if arr[i] < 3:
            continue

        for j in range(i - 1, -1, -1):
            if arr[j] < arr[i] // 2:
                break

            if arr[i] - arr[j] in indexes:
                k = indexes[arr[i] - arr[j]]
                if k >= j:
                    continue

                if (k, j) in dp:
                    dp[(j, i)] = dp[(k, j)] + 1
                else:
                    dp[(j, i)] = 3

                res = max(res, dp[(j, i)])

    return res

