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

def removeStonesDFS(stones: List[List[int]]) -> int:
    if len(stones) < 2:
        return 0

    adj = defaultdict(set)

    for i in range(len(stones)):
        for j in range(len(stones)):
            if i == j:
                continue
            elif stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                adj[i].add(j)
                adj[j].add(i)

    visited = set()
    num_connected = 0

    def dfs(node):
        if node in visited:
            return

        visited.add(node)
        for neighbor in adj[node]:
            dfs(neighbor)

    for i in range(len(stones)):
        if i not in visited:
            dfs(i)
            num_connected += 1

    return len(stones) - num_connected

