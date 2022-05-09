import json
from misc import TreeNode

class Codec:

    def serialize(self, root: TreeNode) -> str:
        values = []

        def traverse(node: TreeNode):
            if not node:
                values.append('null')
                return

            values.append(str(node.val))
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        serialized = '[' + ','.join(values) + ']'
        return serialized

    def deserialize(self, data: str) -> TreeNode:
        values = json.loads(data)
        self.i = 0

        def build_tree():
            if values[self.i] is None:
                self.i += 1
                return None

            node = TreeNode(values[self.i])
            self.i += 1
            node.left = build_tree()
            node.right = build_tree()
            return node

        return build_tree()
