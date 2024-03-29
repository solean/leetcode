from typing import List
from functools import cmp_to_key

class VerifyingAlienDictionary():

    def is_alien_sorted(self, words: List[str], order: str) -> bool:
        self.order = order

        s = sorted(words, key=cmp_to_key(self.compare))
        print(s)

        return words == s

    def compare(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        else:
            end = min(len(word1), len(word2))
            for i in range(end):
                ch1 = word1[i]
                ch2 = word2[i]

                if ch1 == ch2:
                    continue
                else:
                    if self.order.index(word1[i]) > self.order.index(word2[i]):
                        return 1
                    else:
                        return -1

            if len(word1) == end:
                return -1
            else:
                return 1

