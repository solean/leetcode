from typing import List

def mergeArrays(nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
    i, j = 0, 0
    res = []

    while i < len(nums1) and j < len(nums2):
        id1, val1 = nums1[i]
        id2, val2 = nums2[j]

        if id1 == id2:
            res.append([id1, val1 + val2])
            i += 1
            j += 1
        elif id1 < id2:
            res.append([id1, val1])
            i += 1
        else:
            res.append([id2, val2])
            j += 1

    if i < len(nums1):
        res.extend(nums1[i:])
    if j < len(nums2):
        res.extend(nums2[j:])

    return res

