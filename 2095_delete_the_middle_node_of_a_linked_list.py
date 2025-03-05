from misc import ListNode

def deleteMiddle(head: ListNode) -> ListNode:
    n = 0
    node = head
    while node:
        node = node.next
        n += 1

    if n < 2:
        return None

    node = head
    for _ in range(n // 2 - 1):
        node = node.next

    if node.next.next:
        node.next = node.next.next
    else:
        node.next = None

    return head

