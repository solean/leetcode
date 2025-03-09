
def maximumSwap(num: int) -> int:
    digits = list(str(num))
    largest_seen_idx = len(digits) - 1
    swap_1, swap_2 = -1, -1

    for i in range(len(digits) - 2, -1, -1):
        if digits[i] > digits[largest_seen_idx]:
            largest_seen_idx
        elif digits[i] < digits[largest_seen_idx]:
            swap_1 = i
            swap_2 = largest_seen_idx

    if swap_1 != -1:
        digits[swap_1], digits[swap_2] = digits[swap_2], digits[swap_1]

    return int("".join(digits))

