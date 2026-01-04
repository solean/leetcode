from typing import List
import math

def sumFourDivisors(nums: List[int]) -> int:
    res = 0

    for n in nums:
        divisors = [1, n]
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                divisors.append(i)
                if n // i != i:
                    divisors.append(n // i)
                if len(divisors) > 4:
                    break

        if len(divisors) == 4:
            res += sum(divisors)

    return res

