from typing import List
from collections import defaultdict

def queryResults(limit: int, queries: List[List[int]]) -> List[int]:
    balls = defaultdict(int)
    color_freqs = defaultdict(int)
    num_distinct = 0
    res = []

    for ball, color in queries:
        prev_color = balls[ball]
        if prev_color:
            color_freqs[prev_color] -= 1
            if color_freqs[prev_color] == 0:
                num_distinct -= 1

        balls[ball] = color
        if not color_freqs[color]:
            num_distinct += 1
        color_freqs[color] += 1

        res.append(num_distinct)

    return res

