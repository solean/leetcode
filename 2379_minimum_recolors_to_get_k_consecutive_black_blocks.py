
def minimumRecolors(blocks: str, k: int) -> int:
    n = len(blocks)

    whites = blocks[:k].count("W")
    min_whites = whites

    for i in range(n - k):
        if blocks[i] == "W":
            whites -= 1
        if blocks[i + k] == "W":
            whites += 1
        min_whites = min(min_whites, whites)

    return min_whites

