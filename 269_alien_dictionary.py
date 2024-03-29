from typing import List

def alien_order(words: List[str]) -> str:
    adj = {}
    for w in words:
        for ch in w:
            adj[ch] = set()

    for i in range(len(words) - 1):
        w1 = words[i]
        w2 = words[i + 1]
        
        min_len = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""

        for j in range(min_len):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break

    visited = set()
    path = set()
    result = []

    def dfs(c):
        if c in visited or c in path:
            return c in path

        visited.add(c)
        path.add(c)

        for neighbor in adj[c]:
            if dfs(neighbor):
                return True

        path.remove(c)
        result.append(c)
    
    for ch in adj:
        if dfs(ch):
            return ""

    return ''.join(reversed(result))