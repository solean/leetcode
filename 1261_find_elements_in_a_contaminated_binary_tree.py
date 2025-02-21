from misc import TreeNode

class FindElements:

    def __init__(self, root: TreeNode):
        root.val = 0
        self.root = root
        self.has = set([0])

        def dfs(node):
            if node.left:
                node.left.val = 2 * node.val + 1
                self.has.add(node.left.val)
                dfs(node.left)
            if node.right:
                node.right.val = 2 * node.val + 2
                self.has.add(node.right.val)
                dfs(node.right)

        dfs(self.root)

    def find(self, target: int) -> bool:
        return target in self.has

