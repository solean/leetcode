from typing import List
from collections import deque

def deckRevealedIncreasing(deck: List[int]) -> List[int]:
    n = len(deck)
    q = deque([i for i in range(n)])
    deck.sort()
    result = [0] * n

    for i in range(n):
        idx = q.popleft()
        result[idx] = deck[i]

        if q:
            next_card = q.popleft()
            q.append(next_card)
    
    return result

