
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

def clone_graph(node):
    if not node:
        return None

    clones = {}

    def clone(node):
        if node in clones:
            return clones[node]

        copy = Node(node.val)
        clones[node] = copy

        for neighbor in node.neighbors:
            copy.neighbors.append(clone(neighbor))

        return copy

    return clone(node)
