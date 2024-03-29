from misc import TreeNode

def invert_tree(root: TreeNode) -> TreeNode:
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
        return root
