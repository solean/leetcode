from typing import List
from collections import deque

def openLock(deadends: List[int], target: str) -> int:
    q = deque()
    q.append(("0000", 0))
    visited = set()
    visited.add("0000")
    deadends_set = set(deadends)

    while q:
        s, n = q.popleft()

        if s == target:
            return n
        
        if s in deadends_set:
            continue
        
        for i in range(4):
            for direction in (-1, 1):
                l = list(s)
                new_digit = (int(l[i]) + direction) % 10
                l[i] = str(new_digit)
                new_str = ''.join(l)
                if new_str not in visited:
                    q.append((new_str, n + 1))
                    visited.add(new_str)
        
    return -1
