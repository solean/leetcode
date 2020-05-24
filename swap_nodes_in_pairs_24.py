from misc import ListNode, stringify_list

def swap_pairs(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head

    node = head
    temp = node.next
    if node.next.next:
        node.next = node.next.next
    else:
        temp.next = node
        temp.next.next = None
        return temp

    temp.next = node
    node = node.next
    head = temp
    prev = head.next

    while node.next:
        prev.next = node.next
        temp = None
        if node.next.next:
            temp = node.next.next

        prev.next.next = node
        if temp:
            node.next = temp
            prev = node
            node = temp
        else:
            node.next = None
            break

    return head

