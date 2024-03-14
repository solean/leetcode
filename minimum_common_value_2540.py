from typing import List

def getCommon(nums1: List[int], nums2: List[int]) -> int:
    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):
        n1, n2 = nums1[i], nums2[j]

        if n1 < n2:
            i += 1
        elif n2 < n1:
            j += 1
        else:
            return n1
    
    return -1
