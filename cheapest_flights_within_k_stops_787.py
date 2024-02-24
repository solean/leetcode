from typing import List
from collections import deque

def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    adj = defaultdict(list)
    for frm, to, price in flights:
        adj[frm].append((to, price))

    min_price_found = [0] * n
    
    q = deque()
    q.append((src, 0, 0))

    found = False
    min_price = float('inf')

    while q:
        node, cost, stops_so_far = q.popleft()

        if node == dst and stops_so_far <= k + 1:
            found = True
            min_price = min(min_price, cost)
            continue
        
        possible_flights = adj[node]
        for dest, price in possible_flights:
            if min_price_found[dest] == 0 or cost + price < min_price_found[dest]:
                q.append((dest, cost + price, stops_so_far + 1))
                min_price_found[dest] = cost + price

    
    return min_price if found else -1
