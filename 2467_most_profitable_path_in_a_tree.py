from typing import List
from collections import defaultdict, deque

def mostProfitablePath(edges: List[List[int]], bob: int, amount: List[int]) -> int:
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    bob_dist = [-1] * len(amountj)
    bob_visited = set()

    def bob_dfs(node, path):
        bob_visited.add(node)
        path.append(node)

        if node == 0:
            for i, n in enumerate(path):
                bob_dist[n] = 1
            return

        for nei in adj[node]:
            if nei not in bob_visited:
                bob_dfs(nei, path)

        # backtrack
        path.pop()

    bob_dfs(bob, [])

    max_profit = float("-inf")
    q = deque([(0, 0)])
    alice_visited = set()
    depth = 0

    while q:
        for _ in range(len(q)):
            node, curr_profit = q.popleft()
            alice_visited.add(node)

            if bob_dist[node] == -1 or depth < bob_dist[node]:
                curr_profit += amount[node]
            elif depth == bob_dist[node]:
                # split amount
                curr_profit += amount[node] // 2

            is_leaf = True
            for nei in adj[node]:
                if nei not in alice_visited:
                    is_leaf = False
                    q.append((nei, curr_profit))

            if is_leaf:
                max_profit = max(max_profit, curr_profit)

        depth += 1

    return max_profit

