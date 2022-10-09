from misc import TreeNode


def has_path_sum(root: TreeNode, target: int) -> bool:

    def dfs(node: TreeNode, sum_left: int) -> bool:
        if not node:
            return False
        elif not node.left and not node.right:
            return node.val == sum_left
        else:
            left = dfs(node.left, sum_left - node.val)
            right = dfs(node.right, sum_left - node.val)
            return left or right

    return dfs(root, target)
