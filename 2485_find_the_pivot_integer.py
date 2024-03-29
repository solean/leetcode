
def pivotInteger(n: int) -> int:
    if n == 1:
        return 1

    total_sum = (n * (n + 1)) // 2
    prefix_sum = 0

    for i in range(1, n):
        if prefix_sum == total_sum - prefix_sum - i:
            return i
        
        prefix_sum += i

    return -1
