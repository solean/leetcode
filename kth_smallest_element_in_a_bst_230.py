from misc import TreeNode

def kthSmallest(root: TreeNode, k: int) -> int:
    values = []

    def inorder(node: TreeNode):
        if not node:
            return

        inorder(node.left)
        values.append(node.val)
        inorder(node.right)

    inorder(root)
    return values[k - 1]
