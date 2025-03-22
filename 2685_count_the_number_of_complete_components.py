from typing import List
from collections import defaultdict

class Solution:

    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])

        return self.parents[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            self.parents[root1] = root2

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        self.parents = [i for i in range(n)]

        for a, b in edges:
            self.union(a, b)

        components = set()
        for i in range(n):
            root = self.find(i)
            components.add(root)

        num_edges = defaultdict(int)
        nodes = defaultdict(set)
        for a, b in edges:
            component = self.find(a)
            num_edges[component] += 1
            nodes[component].add(a)
            nodes[component].add(b)

        res = 0
        for component in components:
            num_nodes = len(nodes[component])
            if num_edges[component] == (num_nodes * (num_nodes - 1) / 2):
                res += 1

        return res

