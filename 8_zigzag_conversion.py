
def zigzag_converter(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    rows = [''] * numRows
    i = 0
    down = True

    for ch in s:
        rows[i] += ch

        if i == 0:
            down = True
        elif i == numRows - 1:
            down = False

        i += 1 if down else -1

    zigzag = ''.join(rows)
    return zigzag

