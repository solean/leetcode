from typing import List
from misc import ListNode, MinHeap

def merge_k_lists(lists: List[ListNode]) -> ListNode:
    output = None
    output_head = None

    if len(lists) == 0:
        return None
    elif len(lists) == 1:
        return lists[0]

    heap = None

    # Insert all ListNode values into our MinHeap
    for node in lists:
        while node:
            v = node.val
            if heap is None:
                heap = MinHeap(v)
            else:
                heap.insert(v)
            node = node.next

    if heap is None:
        return None

    # Pop values off of the heap 1 by 1 to assemble merged list
    popped = heap.pop()
    while popped is not None:
        if output is None:
            output = ListNode(popped)
            output_head = output
        else:
            output.next = ListNode(popped)
            output = output.next
        popped = heap.pop()

    return output_head

