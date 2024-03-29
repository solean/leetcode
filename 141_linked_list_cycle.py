from misc import ListNode

def has_cycle(head: ListNode) -> bool:
    if not head or not head.next:
        return False

    seen = {}
    node = head

    while node.next:
        if node in seen:
            return True
        else:
            seen[node] = True

    return False

def has_cycle_optimal(head: ListNode) -> bool:
    if not head or not head.next:
        return False

    slow = head
    fast = head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False