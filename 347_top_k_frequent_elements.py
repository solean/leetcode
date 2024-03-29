from typing import List

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    d = {}

    for n in nums:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1

    freq = sorted(d.items(), key=lambda x: x[1], reverse=True)
    res = []

    for i in range(k):
        res.append(freq[i][0])

    return res

def another_solution(nums: List[int], k: int) -> List[int]:
    d = {}

    for n in nums:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1

    bucket = [[] for i in range(len(nums) + 1)]

    for key, count in d.items():
        bucket[count].append(key)

    for i in range(len(bucket) - 1, 0, -1):
        if bucket[i]:
            freq += bucket[i]

            if len(freq) >= k:
                return freq[:k]

