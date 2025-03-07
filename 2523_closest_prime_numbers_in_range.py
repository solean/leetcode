from typing import List

def closestPrimes(left: int, right: int) -> List[int]:
    prime = [True] * (right + 1)
    prime[1] = False
    # Sieve of Eratosthenes
    for n in range(2, right):
        if prime[n]:
            for i in range(n * n, right + 1, n):
                prime[i] = False

    primes_between = [i for i in range(left, right + 1) if prime[i]]
    min_diff = float("inf")
    res = []

    for i in range(len(primes_between) - 1):
        diff = primes_between[i + 1] - primes_between[i]
        if diff < min_diff:
            res = [primes_between[i], primes_between[i + 1]]
            min_diff = diff

    return res or [-1, -1]

