from typing import List

def is_valid_sudoku(board: List[List[str]]) -> bool:
    valid = True

    # check rows
    for row in board:
        if not is_row_valid(row):
            valid = False
            break
    
    # check columns
    for i in range(0, 9):
        column = [row[i] for row in board]
        if not is_row_valid(column):
            valid = False
            break

    # check squares
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            if not is_square_valid(board, (i, j)):
                valid = False
                break

    return valid

def is_row_valid(row: List[str]) -> bool:
    valid = True
    dup_map = {}

    for s in row:
        if s == '.':
            continue
        n = int(s)
        if n > 9 or n < 1:
            valid = False
            break
        elif n in dup_map:
            valid = False
            break
        else:
            dup_map[n] = True


    return valid

def is_square_valid(board, top_left_coord):
    x = top_left_coord[0]
    y = top_left_coord[1]

    square_values = []
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            square_values.append(board[i][j])
    
    valid = is_row_valid(square_values)
    return valid

