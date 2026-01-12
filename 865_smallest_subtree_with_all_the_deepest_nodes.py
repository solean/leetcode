from misc import TreeNode

def subtreeWithAllDeepest(root: TreeNode) -> TreeNode:
    deep_level = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        deep_level = level

    if len(deep_level) == 1:
        return deep_level[0]

    # find LCA of first and last nodes of deepest level
    def dfs(node, p, q):
        if not node:
            return None

        if node == p:
            return node
        elif node == q:
            return node

        left_tree = dfs(node.left, p, q)
        right_tree = dfs(node.right, p, q)

        if left_tree and right_tree:
            return node
        else:
            return left_tree or right_tree

    return dfs(root, deep_level[0], deep_level[-1])

