import heapq

def clearStars(s: str) -> str:
    res = ""
    minheap = []
    remove = set()

    for i, ch in enumerate(s):
        if ch == "*":
            _, idx = heapq.heappop(minheap)
            remove.add(i)
            remove.add(-idx)
        else:
            heapq.heappush(minheap, (ch, -i))

    for i, ch in enumerate(s):
        if i not in remove:
            res += ch

    return res

