from typing import List

# O(n^2) -> TOO SLOW
def max_area_bad(height: List[int]) -> int:
    l = len(height)
    max = 0

    for i in range(0, l):
        for j in range(i + 1, l):
            area = (j - i) * min(height[i], height[j])
            if area > max:
                max = area

    return max

def max_area(height: List[int]) -> int:
    max = 0
    i = 0
    j = len(height) - 1

    while i < j:
        hi = height[i]
        hj = height[j]
        if hi > hj:
            area = (j - i) * hj
            j -= 1
        else:
            area = (j - i) * hi
            i += 1
        
        if area > max:
            max = area

    return max

