from typing import List

class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]

    def union(self, a, b):
        a_rep = self.find(a)
        b_rep = self.find(b)
        if a_rep != b_rep:
            self.parents[a_rep] = b_rep

    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

def countComponents(n: int, edges: List[List[int]]) -> int:
    uf = UnionFind(n)

    for a, b in edges:
        uf.union(a, b)

    component_reps = set()
    for i in range(n):
        rep = uf.find(i)
        component_reps.add(i)
    return len(component_reps)

