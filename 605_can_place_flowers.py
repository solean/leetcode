from typing import List

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    if n == 0:
        return True
    if len(flowerbed) < 3:
        return sum(flowerbed) == 0 and n < 2

    count = 0

    for i in range(len(flowerbed)):
        if flowerbed[i] == 1:
            continue

        if (i == 0 or not flowerbed[i - 1]) and (i == len(flowerbed) - 1 or not flowerbed[i + 1]):
            count += 1
            flowerbed[i] = 1

    return count >= n

