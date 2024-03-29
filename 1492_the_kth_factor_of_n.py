
def kthFactor(n: int, k: int) -> int:
    factors = [i for i in range(1, n + 1) if n % i == 0]
    return factors[k - 1] if len(factors) >= k else -1

