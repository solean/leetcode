from typing import List
from misc import TreeNode
from collections import deque

def zigzagLevelOrder(root: TreeNode) -> List[List[int]]:
    levels = []
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
                if len(levels) % 2 != 0:
                    level.reverse()
                levels.append(level)
    
    return levels
