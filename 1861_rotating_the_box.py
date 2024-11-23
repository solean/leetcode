from typing import List

def rotateTheBox(box: List[List[str]]) -> List[List[str]]:
    m = len(box)
    n = len(box[0])

    for i in range(m):
        count_rocks = 0
        for j in range(n):
            if box[i][j] == "#":
                count_rocks += 1
                box[i][j] = "."
            elif box[i][j] == "*" and count_rocks:
                # go back and fill in stones
                for k in range(j - 1, j - count_rocks - 1, -1):
                    box[i][k] = "#"

                count_rocks = 0

            if j == n - 1 and count_rocks:
                for k in range(j, j - count_rocks, -1):
                    box[i][k] = "#"

    rotated = [["." for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            rotated[i][j] = box[j][i]
        rotated[i].reverse()

    return rotated

