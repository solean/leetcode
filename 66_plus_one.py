from typing import List

def plus_one(digits: List[int]) -> List[int]:
    if digits[-1] == 9:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break

        if digits[0] == 0:
            digits = [1] + digits

        return digits
    else:
        digits[-1] += 1
        return digits

