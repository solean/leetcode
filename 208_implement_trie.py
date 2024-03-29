
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = True

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node.children[ch]
        
        return node.end

    def search(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node.children[ch]
        
        return True