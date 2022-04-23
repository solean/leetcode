from typing import List

# Modify nums1 in-place
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i, j = m - 1, n - 1
    z = m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[z] = nums1[i]
            i -= 1
        else:
            nums1[z] = nums2[j]
            j -= 1

        z -= 1

    return nums1

