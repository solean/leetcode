from misc import TreeNode
from typing import List

def buildTree(inorder: List[int], postorder: List[int]) -> TreeNode:
    if not inorder or not postorder:
        return None

    root_val = postorder[-1]
    root = TreeNode(val=root_val)
    i = inorder.index(root_val)

    root.left = buildTree(inorder[:i], postorder[:i])
    root.right = buildTree(inorder[i+1:], postorder[i:-1])

    return root
