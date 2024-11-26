from misc import Node

def treeToDoublyList(root: Node) -> Node:
    if not root:
        return None

    first = None
    last = None

    def traverse(node):
        nonlocal first, last

        if not node:
            return

        traverse(node.left)

        if last:
            # link prev node with current
            last.right = node
            node.left = last
        else:
            # keep the first node (smallest val) to close list later on
            first = node

        last = node
        traverse(node.right)

    traverse(root)

    # close doubly linked list
    last.right = first
    first.left = last

    return first

