from misc import TreeNode

def goodNodes(root: TreeNode) -> int:
    num_good = 1 + iterate(root.left, root.val) + iterate(root.right, root.val)
    return num_good


def iterate(node: TreeNode, highest_val: int) -> int:
    if not node:
        return 0

    if not node.left and not node.right:
        return 1 if node.val >= highest_val else 0

    if node.val >= highest_val:
        return 1 + iterate(node.left, node.val) + iterate(node.right, node.val)
    else:
        return iterate(node.left, highest_val) + iterate(node.right, highest_val)

