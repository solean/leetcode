from typing import List

def findDifferentBinaryString(nums: List[str]) -> str:
    n = len(nums)
    num_set = set(nums)
    res = [""]

    def recurse(curr):
        if len(curr) == n:
            if curr not in num_set:
                res[0] = curr
            return

        if not res[0]:
            recurse(curr + "0")
            recurse(curr + "1")

    recurse("")
    return res[0]

