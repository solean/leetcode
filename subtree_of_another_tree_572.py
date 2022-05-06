from misc import TreeNode

def is_subtree(root: TreeNode, subRoot: TreeNode) -> bool:

    def is_same(p: TreeNode, q: TreeNode) -> bool:
        if not p or not q:
            return p is None and q is None
        if p.val != q.val:
            return False
        return is_same(p.left, q.left) and is_same(p.right, q.right)

    if not subRoot:
        return True
    if not root:
        return False

    if is_same(root, subRoot):
        return True
    else:
        return is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot)
