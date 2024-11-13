
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

def lowestCommonAncestor(p: Node, q: Node) -> Node:

    def dfs(node, traversal):
        if node:
            if isinstance(traversal, set):
                traversal.add(node)
            else:
                traversal.append(node)
            if node.parent:
                dfs(node.parent, traversal)

    p_traversal = set()
    dfs(p, p_traversal)
    q_traversal = []
    dfs(q, q_traversal)

    for node in q_traversal:
        if node in p_traversal:
            return node

    return None

