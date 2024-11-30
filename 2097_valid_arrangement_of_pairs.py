from typing import List
from collections import defaultdict, deque

def validArrangement(pairs: List[List[int]]) -> List[List[int]]:
    adj = defaultdict(deque)
    indegree = defaultdict(int)
    outdegree = defaultdict(int)
    result = []

    for start, end in pairs:
        adj[start].append(end)
        outdegree[start] += 1
        indegree[end] += 1

    def dfs(node):
        while adj[node]:
            nxt = adj[node].popleft()
            dfs(nxt)
        result.append(node)

    startnode = -1
    for node in outdegree:
        if outdegree[node] == indegree[node] + 1:
            startnode = node
            break
    if startnode == -1:
        startnode = pairs[0][0]

    dfs(startnode)

    result.reverse()
    resultpairs = []
    for i in range(len(result) - 1):
        resultpairs.append([result[i], result[i + 1]])

    return resultpairs

