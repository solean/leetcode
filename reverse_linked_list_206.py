from misc import ListNode

def reverse(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    prev = head
    head = head.next
    prev.next = None

    while head:
        nxt = head.nxt
        head.next = prev
        prev = head
        if nxt:
            head = nxt
        else:
            break

    return head
