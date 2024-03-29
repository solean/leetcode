from typing import List
from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def level_order(root: Node) -> List[List[int]]:
    traversal = []
    q = deque([root])

    while q:
        level = []

        for _ in range(len(q)):
            curr = q.popleft()
            if curr:
                level.append(curr.val)
                q += curr.children

        if level:
            traversal.append(level)

    return traversal
