from typing import List

class Node:

    def __init__(self):
        self.children = {}
        self.end = False

class SuffixTree:

    def __init__(self, words: List[str]):
        self.root = Node()

        for word in words:
            self.insert(word)

    def insert(self, word: str) -> None:
        node = self.root

        for ch in reversed(word):
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]

        node.end = True

    def get_node_under_root(self, ch: str) -> Node:
        if ch in self.root.children:
            return self.root.children[ch]
        else:
            return None


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = SuffixTree(words)
        self.stream = []

    def query(self, letter: str) -> bool:
        self.stream.append(letter)

        node = self.trie.get_node_under_root(letter)
        if node:
            if node.end:
                return True

            # look backwards through stream
            for i in range(len(self.stream) - 2, -1, -1):
                ch = self.stream[i]
                if ch in node.children:
                    node = node.children[ch]
                    if node.end:
                        return True
                else:
                    break

        return False

