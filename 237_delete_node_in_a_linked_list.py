
def deleteNode(node):
    while node.next:
        node.val = node.next.val

        if not node.next.next:
            node.next = None
            break

        node = node.next

