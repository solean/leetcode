import heapq
from collections import Counter

def repeatLimitedString(s: str, repeatLimit: int) -> str:
    if not s:
        return ""

    s = "".join(sorted(s, reverse=True))
    counts = Counter(s)
    res = []

    max_heap = [-1 * (ord(ch) - 97) for ch in counts.keys()]
    heapq.heapify(max_heap)

    while max_heap:
        item = heapq.heappop(max_heap)
        ch = chr((-1 * item) + 97)

        repeats = 0
        while counts[ch] and repeats < repeatLimit:
            res.append(ch)
            counts[ch] -= 1
            repeats += 1

        if counts[ch]:
            if max_heap:
                next_largest = heapq.heappop(max_heap)
                next_largest_ch = chr((-1 * next_largest) + 97)

                res.append(next_largest_ch)
                counts[next_largest_ch] -= 1

                if counts[next_largest_ch]:
                    heapq.heappush(max_heap, next_largest)
            else:
                break

            heapq.heappush(max_heap, item)

    return "".join(res)

