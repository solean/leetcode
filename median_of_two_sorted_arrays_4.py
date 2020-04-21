from typing import List
import math
import unittest

# This solution has O(n+m) time. Overall run time complexity should be O(log (m+n))
def findMedianSortedArraysBad(nums1: List[int], nums2: List[int]) -> float:
    combined = combine_sorted_arrays(nums1, nums2)
    l = len(combined)

    if l % 2 == 0:
        i = int(l / 2)
        median = (combined[i] + combined[i - 1]) / 2
    else:
        median = float(combined[math.floor(l / 2)])

    return median

def combine_sorted_arrays(nums1: List[int], nums2: List[int]) -> List[int]:
    combined = []
    l1 = len(nums1)
    l2 = len(nums2)
    i = 0
    j = 0

    while i < l1 or j < l2:
        n1 = nums1[i] if i < l1 else None
        n2 = nums2[j] if j < l2 else None

        if n1 is None and n2 is None:
            break
        elif n1 is None:
            combined.extend(nums2[j:])
            break
        elif n2 is None:
            combined.extend(nums1[i:])
            break
        else:
            if n1 == n2:
                combined.extend([n1, n2])
                i += 1
                j += 1
            elif n1 > n2:
                combined.append(n2)
                j += 1
            else:
                combined.append(n1)
                i += 1
    
    return combined


# Faster solution
def findMedianSortedArrays(nums1: List[int], nums2: List[int]):
    l = len(nums1) + len(nums2)
    if l == 2:
        combined = nums1 + nums2
        return (combined[0] + combined[1]) / 2

    stop = math.floor(l / 2) + 1 if l % 2 != 0 else int(l / 2) + 1
    seen = []
    i = 0
    j = 0

    while len(seen) < stop:
        n1 = nums1[i] if i < len(nums1) else None
        n2 = nums2[j] if j < len(nums2) else None

        if n1 == n2:
            if len(seen) + 2 > stop:
                seen.append(n1)
                break
            else:
                seen.extend([n1, n2])
                i += 1
                j += 1
        elif n1 is None and n2 is not None:
            seen.append(n2)
            j += 1
        elif n2 is None and n1 is not None:
            seen.append(n1)
            i += 1
        elif n1 > n2:
            seen.append(n2)
            j += 1
        elif n1 is not None:
            seen.append(n1)
            i += 1
    
    median = float(seen[-1]) if l % 2 != 0 else (seen[-2] + seen[-1]) / 2

    return median



class TestFindMedianSortedArrays(unittest.TestCase):

    def test_1(self):
        self.assertEqual(findMedianSortedArraysBad([1, 3], [2]), 2.0)

    def test_2(self):
        self.assertEqual(findMedianSortedArraysBad([1, 2], [3, 4]), 2.5)

    def test_3(self):
        self.assertEqual(findMedianSortedArraysBad([3, 4], [1, 2]), 2.5)

    def test_4(self):
        self.assertEqual(findMedianSortedArraysBad([1, 2, 2], [1, 2, 3]), 2.0)


if __name__ == '__main__':
    unittest.main()
