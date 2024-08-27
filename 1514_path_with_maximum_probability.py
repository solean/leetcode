from typing import List
from collections import defaultdict
import heapq

def maxProbability(n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
    adj = defaultdict(list)
    probs = dict()
    max_prob = [0] * n
    max_prob[start_node] = 1

    for i in range(len(edges)):
        a, b = edges[i]
        adj[a].append(b)
        adj[b].append(a)
        probs[(a, b)] = succProb[i]
        probs[(b, a)] = succProb[i]

    maxheap = []
    heapq.heappush(maxheap, (-1, start_node))

    while maxheap:
        neg_prob, node = heapq.heappop(maxheap)
        curr_prob = -neg_prob

        if node == end_node:
            return curr_prob

        if curr_prob < max_prob[node]:
            continue

        for neighbor in adj[node]:
            new_prob = curr_prob * probs[(node, neighbor)]

            if new_prob > max_prob[neighbor]:
                max_prob[neighbor] = new_prob
                heapq.heappush(maxheap, (-new_prob, neighbor))

    return 0

