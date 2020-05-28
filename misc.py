from typing import List


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def stringify_list(l: ListNode) -> str:
    s = ''
    while l:
        s += f' -> {l.val}' if s else f'{l.val}'
        l = l.next
    return s


# Binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

