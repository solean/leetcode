from misc import ListNode
from collections import defaultdict

def pairSum(head: ListNode) -> int:
    n = 0
    node = head
    while node:
        n += 1
        node = node.next

    max_sum = float("-inf")
    sum_map = defaultdict(int)
    node = head
    for i in range(n):
        if i < n // 2:
            sum_map[i] = node.val
        else:
            sum_map[n - i - 1] += node.val
            max_sum = max(max_sum, sum_map[n - i - 1])

        node = node.next

    return max_sum

