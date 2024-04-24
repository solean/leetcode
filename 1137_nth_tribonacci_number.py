
def tribonacci(n: int) -> int:
    arr = [0, 1, 1]

    if n < 3:
        return arr[n]

    for i in range(3, n + 1):
        trib = arr[i - 1] + arr[i - 2] + arr[i - 3]
        arr.append(trib)
    
    return arr[-1]
    