from typing import List
from misc import TreeNode
from collections import deque

def level_order(root: TreeNode) -> List[List[int]]:
    traversal = []
    q = deque([root])

    while q:
        level = []

        for _ in range(len(q)):
            curr = q.popleft()
            if curr:
                level.append(curr.val)
                q.append(curr.left)
                q.append(curr.right)

        if level:
            traversal.append(level)

    return traversal
