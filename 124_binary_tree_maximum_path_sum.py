from misc import TreeNode

class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        self.mx = root.val
        self.traverse(root)
        return self.mx

    def traverse(self, node: TreeNode) -> int:
        if not node:
            return 0

        left = max(0, self.traverse(node.left))
        right = max(0, self.traverse(node.right))
        self.mx = max(self.mx, left + right + node.val)
        return node.val + max(left, right)
