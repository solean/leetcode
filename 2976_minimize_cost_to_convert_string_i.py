from typing import List
from collections import defaultdict
import heapq

def minimumCost(source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

    def dijkstra(start, adj):
        mincosts = [float("inf")] * 26
        minheap = [(0, start)]

        while minheap:
            curr_cost, ch = heapq.heappop(minheap)
            for node, node_cost in adj[ch]:
                n = ord(node) - 97

                new_cost = curr_cost + node_cost
                if new_cost < mincosts[n]:
                    mincosts[n] = new_cost
                    heapq.heappush(minheap, (new_cost, node))

        return mincosts


    adj = defaultdict(list)
    for i in range(len(original)):
        adj[original[i]].append((changed[i], cost[i]))

    mincosts = []
    for i in range(26):
        mincosts.append(dijkstra(chr(i + 97), adj))

    res = 0

    for s, t in zip(source, target):
        if s != t:
            mincost = mincosts[ord(s) - 97][ord(t) - 97]
            if mincost == float("inf"):
                return -1
            res += mincost

    return res

