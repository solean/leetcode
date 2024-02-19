
def is_power_of_two(n: int) -> bool:
    for i in range(31):
        if 2 ** i == n:
            return True
    return False

