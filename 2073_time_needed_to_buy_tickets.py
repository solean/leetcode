from collections import deque
from typing import List

def timeRequiredToBuy(tickets: List[int], k: int) -> int:
    tix = 0
    q = deque()

    for i in range(len(tickets)):
        q.append((i, tickets[i]))

    while q:
        idx, tix_left = q.popleft()

        tix += 1
        tix_left -= 1

        if tix_left > 0:
            q.append((idx, tix_left)) 

        if idx == k and tix_left == 0:
            break

    return tix

def timeRequiredToBuyOptimal(tickets: List[int], k: int) -> int:
    tix = 0

    for i in range(len(tickets)):
        if i <= k:
            tix += min(tickets[k], tickets[i])
        else:
            tix += min(tickets[k] - 1, tickets[i])
    
    return tix
