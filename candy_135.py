from typing import List

def candy(ratings: List[int]) -> int:
    n = len(ratings)
    candies = [1] * n

    # check left neighbors
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # check right neighbors
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
            candies[i] = candies[i + 1] + 1

    return sum(candies)
