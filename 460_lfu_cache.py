from collections import defaultdict

class Node:
    def __init__(self, key: int, val: int, freq: int):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = Node(None, None, 0)
        self.tail = Node(None, None, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def append(self, node: Node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        self.size += 1

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size += 1

    def remove_lru(self) -> Node:
        if self.size == 0:
            return None

        lru = self.head.next
        self.remove(lru)
        return lru

    def getsize(self) -> int:
        return self.size


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freq_lists = defaultdict(DLL)
        self.minfreq = -1
        self.totalsize = 0

    def _remove_and_move_node(self, node: Node):
        self.freq_lists[node.freq].remove(node)

        if self.freq_lists[node.freq].getsize() == 0 and node.freq == self.minfreq:
            self.minfreq = node.freq + 1

        node.freq += 1
        self.freq_lists[node.freq].append(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove_and_move_node(node)
        return node.val

    def put(self, key: int, value: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove_and_move_node(node)
        else:
            if self.totalsize == self.capacity:
                removed_node = self.freq_lists[self.minfreq].remove_lru()
                self.totalsize -= 1
                del self.cache[removed_node.key]

            node = Node(key, value, 1)
            self.cache[key] = node
            self.freq_lists[1].append(node)
            self.minfreq = 1

            self.totalsize += 1

