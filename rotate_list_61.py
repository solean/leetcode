from misc import ListNode

def rotateRight(head: ListNode, k: int) -> ListNode:
    if not head:
        return head

    n = 1
    node = head
    while node.next:
        n += 1
        node = node.next
    tail = node

    num_rotations = k % n
    if not num_rotations:
        return head

    node = head
    for _ in range(n - num_rotations - 1):
        node = node.next
    
    new_head = node.next
    node.next = None
    tail.next = head
    return new_head
