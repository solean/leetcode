from typing import List
from misc import TreeNode

def binary_tree_paths(root: TreeNode) -> List[str]:
    paths = []

    def dfs(node, path):
        if not node: return None

        path.append(node.val)

        if not node.left and not node.right:
            paths.append(path.copy())
        else:
            dfs(node.left, path)
            dfs(node.right, path)

        path.pop()

    dfs(root, [])

    path_strs = []
    for path in paths:
        path_str = ""
        for n in path:
            path_str += str(n) + "->"
        if path_str.endswith("->"):
            path_str = path_str[:-2]
        path_strs.append(path_str)

    return path_strs