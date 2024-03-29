
def maximumOddBinaryNumber(s: str) -> str:
    num_ones, num_zeros = 0, 0

    for ch in s:
        if ch == "1":
            num_ones += 1
        else:
            num_zeros += 1

    return ("1" * (num_ones - 1)) + ("0" * num_zeros) + "1"

