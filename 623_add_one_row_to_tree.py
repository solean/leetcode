from collections import deque

def addOneRow(root: TreeNode, val: int, depth: int) -> TreeNode:
    if depth == 1:
        return TreeNode(val, root, None)

    q = deque([root])
    num_levels = 0

    while q:
        level = []

        for _ in range(len(q)):
            node = q.popleft()
            if node:
                level.append(node)
                q.append(node.left)
                q.append(node.right)

        if level:
            num_levels += 1

        if num_levels == depth - 1:
            for node in level:
                left = node.left
                right = node.right

                node.left = TreeNode(val, left, None)
                node.right = TreeNode(val, None, right)

            break

    return root
