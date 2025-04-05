from typing import List

def subsetXORSum(nums: List[int]) -> int:

    def get_subsets(arr):
        if not arr:
            return [[]]

        subsets = get_subsets(arr[1:])
        return subsets + [[arr[0]] + subset for subset in subsets]

    nums_subsets = get_subsets(nums)

    total = 0
    for subset in nums_subsets:
        if not subset:
            continue

        curr = subset[0]
        for i in range(1, len(subset)):
            curr ^= subset[i]

        total += curr

    return total

