from typing import List

def findNumbers(nums: List[int]) -> int:
    return sum([1 if len(str(n)) % 2 == 0 else 0 for n in nums])

