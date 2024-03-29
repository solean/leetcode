from misc import ListNode

def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    if not head or not head.next:
        return head
    
    node = head
    left_tail = head

    if left > 1:
        for _ in range(left - 2):
            left_tail = left_tail.next
        
        node = left_tail.next
    
    new_inner_tail = node
    prev = None
    for _ in range(left, right + 1):
        if not node:
            break
        
        nxt = node.next or None
        node.next = prev
        prev = node
        node = nxt
    
    left_tail.next = prev
    new_inner_tail.next = node

    return head if left > 1 else prev
