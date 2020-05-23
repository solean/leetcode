from typing import List

def find_substring(s, words):
    output = []
    if len(words) == 0:
        return []

    word_length = len(words[0])
    orig_words_map = dict()
    for w in words:
        if w in orig_words_map:
            orig_words_map[w] += 1
        else:
            orig_words_map[w] = 1

    j = 0
    while j < len(s):
        section = get_section(s[j:j+(len(words)*word_length)], word_length)
        words_map = orig_words_map.copy()
        for w in section:
            if w in words_map:
                if words_map[w] == 1:
                    del words_map[w]
                else:
                    words_map[w] -= 1

                if len(words_map.keys()) == 0:
                    output.append(j)
            else:
                break

        j += 1

    return output


def get_section(s: str, word_length: int) -> List[str]:
    s_words = [s[i:i+word_length] for i in range(0, len(s), word_length)]
    return s_words
 
