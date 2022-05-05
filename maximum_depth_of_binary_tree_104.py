from misc import TreeNode

def max_depth(root: TreeNode) -> int:
    if not root:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))
