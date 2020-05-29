from typing import List
from misc import TreeNode

def preorder_traversal(root: TreeNode) -> List[int]:
    seen = []
    traverse(root, seen)
    return seen

def traverse(node: TreeNode, seen: List[int]):
    if node is not None:
        traverse(node.left, seen)
        traverse(node.right, seen)
        seen.append(node.val)

