import math
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


class MinHeap():
    def __init__(self, root):
        self.heap = [None, root]

    def insert(self, value):
        self.heap.append(value)
        k = len(self.heap) - 1

        while k > 1:
            parent_index = math.floor(k / 2)
            if value < self.heap[parent_index]:
                self.heap[k] = self.heap[parent_index]
                self.heap[parent_index] = value
                k = parent_index
            else:
                break

    def swap_parent_with_left(self, k):
        left = self.heap[k * 2]
        self.heap[k * 2] = self.heap[k]
        self.heap[k] = left
        k = k * 2
        return k

    def swap_parent_with_right(self, k):
        right = self.heap[k * 2 + 1]
        self.heap[k * 2 + 1] = self.heap[k]
        self.heap[k] = right
        k = k * 2 + 1
        return k

    def pop(self):
        if len(self.heap) < 2:
            return self.heap[0]

        root = self.heap[1]
        new_root = self.heap.pop()
        if len(self.heap) == 1:
            return root
        self.heap[1] = new_root

        k = 1
        while k < len(self.heap):
            parent = self.heap[k]
            left_child = None
            right_child = None
            if k * 2 < len(self.heap):
                left_child = self.heap[k * 2]
            if k * 2 + 1 < len(self.heap):
                right_child = self.heap[k * 2 + 1]

            if left_child is None and right_child is None:
                break
            elif left_child is None:
                if parent > right_child:
                    k = self.swap_parent_with_right(k)
                else:
                    break
            elif right_child is None:
                if parent > left_child:
                    k = self.swap_parent_with_left(k)
                else:
                    break
            else:
                if left_child <= right_child and left_child < parent:
                    k = self.swap_parent_with_left(k)
                elif right_child <= left_child and right_child < parent:
                    k = self.swap_parent_with_right(k)
                else:
                    break

        return root


# O(log n) search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + math.floor((high - low) / 2)
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    
    return -1

