from typing import List

def stringShift(s: str, shift: List[List[int]]) -> str:
    total_shifts = 0
    for d, amount in shift:
        if d == 1:
            total_shifts += amount
        else:
            total_shifts -= amount

    total_shifts %= len(s)

    if total_shifts == 0:
        return s

    return s[-total_shifts:] + s[:-total_shifts]

