
def is_happy(n: int) -> bool:

    def get_next(n):
        total = 0
        for digit in list(str(n)):
            total += int(digit)**2
        return total

    slow = n
    fast = get_next(n)
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))

    return fast == 1
