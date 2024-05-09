from typing import List

def maximumHappinessSum(happiness: List[int], k: int) -> int:
    total = 0
    happiness.sort(reverse=True)

    for i in range(k):
        total += max(happiness[i] - i, 0)

    return total

