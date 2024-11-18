from typing import List
from collections import defaultdict

def accountsMerge(accounts: List[List[int]]) -> List[List[str]]:
    adj = defaultdict(list)
    ans = []
    visited = set()

    for acc in accounts:
        email = acc[1]
        for i in range(2, len(acc)):
            adj[email].append(acc[i])
            adj[acc[i]].append(email)

    def dfs(email, merged):
        visited.add(email)
        merged.append(email)
        for e in adj[email]:
            if e not in visited:
                dfs(e, merged)

    for acc in accounts:
        if acc[1] not in visited:
            merged = []
            dfs(acc[1], merged)
            merged.sort()
            merged.insert(0, acc[0])
            ans.append(merged)

    return ans

