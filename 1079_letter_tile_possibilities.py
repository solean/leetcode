
def numTilePossibilities(tiles: str):
    seqs = set()
    used = [False] * len(tiles)

    def recurse(curr):
        seqs.add(curr)

        for i, ch in enumerate(tiles):
            if not used[i]:
                used[i] = True
                recurse(curr + ch)
                used[i] = False

    recurse("")
    return len(seq) - 1

