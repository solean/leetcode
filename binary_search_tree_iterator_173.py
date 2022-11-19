from misc import TreeNode

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.pointer = float('-inf')
        self.traversal = []

    def traverse(self, node: TreeNode):
        if not node: return
        self.traverse(node.left)
        self.traversal.append(node.val)
        self.traverse(node.right)

    def next(self) -> int:
        if self.pointer == float('-inf'):
            self.traverse(self.root)
            self.pointer = 0

        item = self.traversal(self.pointer)
        self.pointer += 1
        return item

    def hasnext(self) -> bool:
        return self.pointer < len(self.traversal)