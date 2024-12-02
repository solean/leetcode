from typing import List
from collections import defaultdict

def checkIfExist(arr: List[int]) -> bool:
    d = defaultdict(int)

    for n in arr:
        if n == 0:
            if 0 in d:
                return True
        elif n * 2 in d or n / 2 in arr:
            return True
        d[n] = True

    return False

