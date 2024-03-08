from misc import ListNode

def deleteDuplicates(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    dummy = ListNode(0, head)
    prev = dummy
    node = head

    while node:
        if node.next and node.val == node.next.val:
            while node.next and node.val == node.next.val:
                node = node.next
            prev.next = node.next
        else:
            prev = prev.next

        node = node.next

    return dummy.next
