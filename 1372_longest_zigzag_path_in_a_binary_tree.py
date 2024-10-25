from misc import TreeNode

def longestZigZag(root: TreeNode) -> int:
    self.max_length = 0

    def dfs(node, length, dir):
        if not node:
            return

        self.max_length = max(self.max_length, length)

        if dir == "left":
            dfs(node.left, length + 1, "right")
            dfs(node.right, 1, "left")
        elif dir == "right":
            dfs(node.right, length + 1, "left")
            dfs(node.left, 1, "right")

    dfs(root, 0, "left")
    dfs(root, 0, "right")
    return self.max_length

