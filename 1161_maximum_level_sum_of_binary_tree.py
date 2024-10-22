from misc import TreeNode
from collections import deque

def maxLevelSum(root: TreeNode) -> int:
    q = deque([root])
    max_level_sum = float('-inf')
    max_level = None
    level_count = 1

    while q:
        level_sum = 0

        for _ in range(len(q)):
            node = q.popleft()
            level_sum += node.val

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        if level_sum > max_level_sum:
            max_level_sum = level_sum
            max_level = level_count

        level_count += 1

    return max_level

