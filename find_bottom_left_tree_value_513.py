from misc import TreeNode
from collections import deque

def findBottomLeftValue(self, root: TreeNode) -> int:
    levels = []
    q = deque([root])

    while q:
        level = []

        for i in range(len(q)):
            node = q.popleft()
            level.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        levels.append(level)
        

    return levels[-1][0]
