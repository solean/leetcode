from misc import TreeNode

def right_side_view(root: TreeNode):
    right_side_nodes = []
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
            right_side_nodes.append(level.pop())

    return right_side_nodes
