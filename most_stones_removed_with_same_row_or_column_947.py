from typing import List
from collections import defaultdict, deque

def removeStones(stones: List[List[int]]) -> int:
    x_neighbors = defaultdict(list)
    y_neighbors = defaultdict(list)

    for stone in stones:
        x_neighbors[stone[0]].append(stone[1])
        y_neighbors[stone[1]].append(stone[0])

    connected = 0
    visited = set()

    for stone in stones:
        x = stone[0]
        y = stone[1]

        if (x, y) not in visited:
            q = deque()
            q.append((x, y))

            while q:
                nxt = q.popleft()
                xo = nxt[0]
                yo = nxt[1]

                if (xo, yo) not in visited:
                    visited.add((xo, yo))

                    for y_neighbor in x_neighbors[xo]:
                        q.append((xo, y_neighbor))
                    
                    for x_neighbor in y_neighbors[yo]:
                        q.append((x_neighbor, yo))

            connected += 1
    
    diff = len(stones) - connected
    return diff