from typing import List
from misc import TreeNode

def constructFromPrePost(preorder: List[int], postorder: List[int]) -> TreeNode:
    postorder_map = {}
    for i, val in enumerate(postorder):
        postorder_map[val] = i

    def recurse(i1, i2, j):
        if i1 > i2:
            return None

        node = TreeNode(val=preorder[i])
        if i1 == i2:
            return node

        left_val = preorder[i1 + 1]
        mid = postorder_map[left_val]
        left_size = mid - j + 1

        node.left = recurse(i1 + 1, i1 + left_size, j)
        node.right = recurse(i1 + left_size + 1, i2, mid + 1)

        return node

    return recurse(0, len(postorder), 0)

