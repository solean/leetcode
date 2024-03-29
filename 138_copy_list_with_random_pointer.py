
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'None' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head: Node) -> Node:
    clone_map = {}
    clone_map[None] = None

    node = head
    while node:
        clone_map[node] = Node(node.val, None, None)
        node = node.next

    node = head
    while node:
        clone = clone_map[node]
        clone.next = clone_map[node.next]
        clone.random = clone_map[node.random]
        node = node.next

    return clone_map[head]
