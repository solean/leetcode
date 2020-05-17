from misc import ListNode, stringify_list

# O(n) but requires two passes
def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    node = head

    num_nodes = 0
    # First pass to find number of nodes
    while node:
        num_nodes += 1
        node = node.next

    # Second pass to remove node
    node = head
    i = 0
    while node:
        if i == 0 and n == num_nodes:
            head = node.next
            return head
        elif i == num_nodes - n - 1:
            node.next = node.next.next
            return head
        else:
            i += 1
            node = node.next

    return head

