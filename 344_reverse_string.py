from typing import List

def reverse_string(s: List[str]) -> None:
    i = 0
    j = len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

    # return

s = ['h', 'e', 'l', 'l', 'o']
expected = ['o', 'l', 'l', 'e', 'h']
reverse_string(s)
print(s)

s = ['H', 'a', 'n', 'n', 'a', 'h']
expected = ['h', 'a', 'n', 'n', 'a', 'H']
reverse_string(s)
print(s)