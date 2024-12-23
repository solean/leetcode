from misc import ListNode

def mergeNodes(head: ListNode) -> ListNode:
    node = head.next
    curr_sum = 0
    new_head = None
    last_new = None

    while node:
        if node.val == 0:
            sum_node = ListNode(val=curr_sum)
            if not new_head:
                new_head = sum_node
            else:
                last_new.next = sum_node

            last_new = sum_node
            curr_sum = 0
        else:
            curr_sum += node.val

        node = node.next

    return new_head

