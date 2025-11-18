from typing import List

def isOneBitCharacter(bits: List[int]) -> bool:
    n = len(bits)
    i = 0
    while i < n - 1:
        if bits[i] == 1:
            if i == n - 2:
                return False
            else:
                i += 2
        else:
            i += 1

    return True

