from typing import List
from misc import ListNode

def splitListToParts(head: ListNode, k: int) -> List[ListNode]:
    n = 0
    lists = []

    node = head
    while node:
        node = node.next
        n += 1
    
    num_in_list = n // k
    num_with_extra = n % k

    curr = head
    for i in range(k):
        lists.append(curr)
        
        curr_list_size = num_in_list + 1 if i < num_with_extra else num_in_list
        for _ in range(curr_list_size - 1):
            if curr:
                curr = curr.next

        if curr:
            nxt = curr.next
            curr.next = None
            curr = nxt

    return lists
