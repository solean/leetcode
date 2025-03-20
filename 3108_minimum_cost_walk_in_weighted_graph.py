from typing import List

class Solution:

    def find(self, node):
        if self.parents[node] == -1:
            return node

        self.parents[node] = self.find(self.parents[node])

        return self.parents[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return

        if self.depth[root1] < self.depth[root2]:
            root1, root2 = root2, root1

        self.parents[root2] = root1

        if self.depth[root1] == self.depth[root2]:
            self.depth[root1] += root1

    def minimumCost(self, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        self.parents = [-1] * n
        self.depth = [0] * n
        component_cost = [-1] * n

        for a, b, weight in edges:
            self.union(a, b)

        for a, b, weight in edges:
            root = self.find(a)
            component_cost[root] &= weight

        res = []
        for src, dest in query:
            # if nodes in diff components, return -1
            if self.find(src) != self.find(dest):
                res.append(-1)
            else:
                root = self.find(src)
                res.append(component_cost[root])

        return res

