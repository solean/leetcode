from misc import ListNode, stringify_list

def delete_duplicates(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head

    last_val = head.val
    last_node = head
    node = head.next
    while node:
        if node.val == last_val:
            node = node.next
            if node is None or node.next is None:
                last_node.next = None
        else:
            last_val = node.val
            last_node.next = node
            last_node = last_node.next
            node = node.next

    return head

