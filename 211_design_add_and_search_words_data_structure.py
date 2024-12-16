
class TrieNode:
    def __init__(self):
        # One for each letter in alphabet
        self.children = [None] * 26
        self.wordEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            ch_int = ord(ch) - 97
            if not curr.children[ch_int]:
                curr.children[ch_int] = TrieNode()

            curr = curr.children[ch_int]

        curr.wordEnd = True

    def search(self, word: str) -> bool:

        def dfs(node, i, path):
            if len(path) >= len(word):
                return node.wordEnd

            curr_ch_int = ord(word[i]) - 97

            if 0 <= curr_ch_int < 26 and node.children[curr_ch_int]:
                return dfs(node.children[curr_ch_int], i + 1, path + word[i])
            elif word[i] == ".":
                for j in range(len(node.children)):
                    if node.children[j]:
                        if dfs(node.children[j], i + 1, path + word[i]):
                            return True

            return False

        return dfs(self.root, 0, "")

