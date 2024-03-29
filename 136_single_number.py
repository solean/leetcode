from typing import List

def single_number(nums: List[int]) -> int:
    seen = dict()

    for n in nums:
        if n in seen:
            del seen[n]
        else:
            seen[n] = True


    return [key for key in seen][0]

