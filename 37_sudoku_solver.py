from typing import List
from collections import defaultdict

def solveSudoku(board: List[List[str]]) -> None:
    row_sets = defaultdict(set)
    col_sets = defaultdict(set)
    subbox_sets = defaultdict(set)
    solved = [False]

    for r in range(9):
        for c in range(9):
            if board[r][c] != ".":
                row_sets[r].add(board[r][c])
                col_sets[c].add(board[r][c])
                box_index = (r // 3) * 3 + c // 3
                subbox_sets[box_index].add(board[r][c])

    def backtrack(r, c):
        if board[r][c] == ".":
            for n in range(1, 10):
                sn = str(n)
                box_index = (r // 3) * 3 + c // 3
                if sn not in row_sets[r] and sn not in col_sets[c] and sn not in subbox_sets[box_index]:
                    board[r][c] = sn
                    row_sets[r].add(sn)
                    col_sets[c].add(sn)
                    subbox_sets[box_index].add(sn)

                    if r == 8 and c == 8:
                        solved[0] = True
                        return
                    else:
                        if c == 8:
                            # end of row, go to next row
                            backtrack(r + 1, 0)
                        else:
                            backtrack(r, c + 1)

                    if solved[0]:
                        return

                    # backtrack
                    board[r][c] = "."
                    row_sets[r].remove(sn)
                    col_sets[c].remove(sn)
                    subbox_sets[box_index].remove(sn)
        else:
            if r == 8 and c == 8:
                solved[0] = True
                return
            else:
                if c == 8:
                    backtrack(r + 1, 0)
                else:
                    backtrack(r, c + 1)

    backtrack(0, 0)

