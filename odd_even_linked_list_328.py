from misc import ListNode

def odd_even_list(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    
    even_head = head.next
    node = head
    i = 0

    while node:
        i += 1

        nxt = node.next
        if not nxt: break
        
        if nxt.next:
            node.next = nxt.next
        else:
            node.next = None
            if i % 2 != 0: break
    
        node = nxt
    
    node.next = even_head
    return head