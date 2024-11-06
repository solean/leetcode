from typing import List
from collections import Counter
import heapq

def topKFrequent(words: List[str], k: int) -> List[str]:
    freqs = Counter(words)
    max_heap = []
    for word in words:
        heapq.heappush(max_heap, (-1 * freqs[word], word))

    res = []
    for _ in range(k):
        neg_freq, word = heapq.heappush(max_heap)
        res.append(word)

    return res

