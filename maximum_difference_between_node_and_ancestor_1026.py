from misc import TreeNode

class Solution:
    def max_ancestor_diff(self, root: TreeNode) -> int:
        self.max_diff = 0

        def dfs(node, biggest, smallest):
            if not node:
                return

            if node.val > biggest:
                biggest = node.val
            if node.val < smallest:
                smallest = node.val

            self.max_diff = max(self.max_diff, abs(biggest - smallest))

            dfs(node.left, biggest, smallest)
            dfs(node.right, biggest, smallest)

        dfs(root, root.val, root.val)
        return self.max_diff