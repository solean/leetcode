from typing import List

class Solution:
    def postorder(self, root) -> List[int]:
        self.traversal = []
        self.traverse(root)
        return self.traversal

    def traverse(self, node):
        if not node:
            return

        for ch in node.children:
            self.traverse(ch)

        self.traversal.append(node.val)

