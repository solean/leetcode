from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def preorder(root: Node) -> List[int]:
    traversal = []

    def dfs(node):
        if node:
            traversal.append(node.val)
            for child in node.children:
                dfs(child)

    dfs(root)

    return traversal
