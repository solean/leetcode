from typing import List

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    ans_set = set()

    nums1_set = set(nums1)
    for n in nums2:
        if n in nums1_set:
            ans_set.add(n)

    return list(ans_set)
