from misc import ListNode

def partition(head: ListNode, x: int) -> ListNode:
    left_dummy = ListNode(0, None)
    left = left_dummy
    right_dummy = ListNode(0, None)
    right = right_dummy

    node = head
    while node:
        nxt = node.next
        node.next = None

        if node.val < x:
            left.next = node
            left = left.next
        else:
            right.next = node
            right = right.next
        
        node = nxt
    
    left.next = right_dummy.next
    return left_dummy.next
