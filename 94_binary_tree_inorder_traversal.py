from typing import List
from misc import TreeNode

def inorder_traversal(root: TreeNode) -> List[int]:
    seen = []
    traverse(root, seen)
    return seen

def traverse(root: TreeNode, seen: List[int]):
    if root is not None:
        traverse(root.left, seen)
        seen.append(root.val)
        traverse(root.right, seen)
