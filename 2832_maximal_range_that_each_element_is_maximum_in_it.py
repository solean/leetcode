from typing import List

def maximumLengthOfRanges(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [0] * n
    left = [-1] * n
    right = [n] * n
    stack = []

    for i in range(n):
        while stack and stack[-1][0] < nums[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1][1]
        stack.append((nums[i], i))

    stack = []
    for i in range(n - 1, -1, -1):
        while stack and stack[-1][0] < nums[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1][1]
        stack.append((nums[i], i))

    for i in range(n):
        res[i] = right[i] - left[i] - 1

    return res

