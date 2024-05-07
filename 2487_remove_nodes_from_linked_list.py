from misc import ListNode

def removeNodes(head: ListNode) -> ListNode:
    vals = []

    node = head
    while node:
        vals.append(node.val)
        node = node.next
    
    for i in range(len(vals) - 2, -1, -1):
        vals[i] = max(vals[i], vals[i + 1])
    
    prev = None
    node = head
    new_head = None
    i = 0
    while node:
        if vals[i] > node.val:
            # remove node
            if prev:
                prev.next = node.next

            if node == new_head:
                new_head = node.next
        else:
            if not new_head:
                new_head = node
            
            prev = node
        
        node = node.next
        i += 1
    
    return new_head
