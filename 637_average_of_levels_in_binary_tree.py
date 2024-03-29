from typing import List
from misc import TreeNode
from collections import deque

def averageOfLevels(root: TreeNode) -> List[float]:
    avgs = []
    q = deque([root])

    while q:
        level = []

        for _ in range(len(q)):
            node = q.popleft()

            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        
        if level:
            avg = sum(level) / len(level)
            avgs.append(avg)

    return avgs
