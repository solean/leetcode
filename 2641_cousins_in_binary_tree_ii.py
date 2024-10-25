from misc import TreeNode
from collections import deque

def replaceValueInTree(root: TreeNode) -> TreeNode:
    q = deque([root])
    levels = []

    while q:
        level_sum = 0

        for _ in range(len(q)):
            node = q.popleft()
            level_sum += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        levels.append(level_sum)

    q = deque([(root, 0)])
    curr_level = 0

    while q:
        for _ in range(len(q)):
            node, sibling_val = q.popleft()
            node.val = levels[curr_level] - node.val - sibling_val

            left_val = node.left.val if node.left else 0
            right_val = node.right.val if node.right else 0
            if node.left:
                q.append((node.left, right_val))
            if node.right:
                q.append((node.right, left_val))

        curr_level += 1

    return root

