from misc import TreeNode

def is_same_tree_iter(p: TreeNode, q: TreeNode) -> bool:
    p_str = stringify_tree(p)
    q_str = stringify_tree(q)

    return p_str == q_str

def stringify_tree(node: TreeNode) -> str:
    current_level = [node]
    tree_str = ''

    while current_level:
        next_level = []
        for node in current_level:
            if node is not None:
                tree_str += str(node.val)
                next_level.append(node.left)
                next_level.append(node.right)
            else:
                tree_str += 'x'

        tree_str += '-'
        current_level = next_level

    return tree_str

# Better recursive solution
def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    if not p or not q:
        return p is None and q is None
    if p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

