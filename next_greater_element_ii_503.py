from typing import List

def next_greater_elements(nums: List[int]) -> List[int]:
    max_num = max(nums)
    stack = []
    next_greater = {}

    i = 0
    while True:
        n = nums[i]

        while stack and n > nums[stack[-1]]:
            next_greater[stack.pop()] = n

        if n == max_num:
            next_greater[i] = -1
        else:
            stack.append(i)

        if len(next_greater) == len(nums):
            break

        if i == len(nums) - 1:
            i = 0
        else:
            i += 1

    output = []
    for i in range(len(nums)):
        output.append(next_greater[i])
    return output