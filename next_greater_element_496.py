from typing import List

def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:

    stack = []
    next_greater = {}

    for n in nums2:
        while stack and n > stack[-1]:
            next_greater[stack.pop()] = n

        stack.append(n)
    
    for left in stack:
        next_greater[left] = -1

    ans = []
    for n in nums1:
        ans.append(next_greater[n])

    return ans