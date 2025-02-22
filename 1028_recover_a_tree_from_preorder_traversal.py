from misc import TreeNode

def recoverFromPreorder(traversal: str) -> TreeNode:
    if not traversal:
        return None

    n = len(traversal)
    levels = []

    i = 0
    while i < n:
        curr_depth = 0
        while traversal[i] == "-":
            curr_depth += 1
            i += 1

        val_str = ""
        while i < n and traversal[i] != "-":
            val_str += traversal[i]
            i += 1

        node = TreeNode(val=int(val_str))

        if curr_depth < len(levels):
            levels[curr_depth] = node
        else:
            levels.append(node)

        if curr_depth:
            parent = levels[curr_depth - 1]
            if not parent.left:
                parent.left = node
            else:
                parent.right = node

        return levels[0]

