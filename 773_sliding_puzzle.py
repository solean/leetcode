from typing import List
from collections import deque
import copy

def slidingPuzzle(board: List[List[int]]) -> int:
    solved = "123450"
    visited = set()
    q = deque()
    q.append((board, 0))
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def to_string(matrix):
        s = ""
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                s += str(matrix[i][j])
        return s

    while q:
        for _ in range(len(q)):
            node, num_moves = q.popleft()
            node_str = to_string(node)
            if node_str in visited:
                continue

            visited.add(to_string(node))

            if node_str == solved:
                return num_moves
            else:
                zx, zy = 0, 0
                for i in range(len(node)):
                    for j in range(len(node[0])):
                        if node[i][j] == 0:
                            zx, zy = i, j
                            break

                for dx, dy in dirs:
                    nx, ny = zx + dx, zy + dy
                    if 0 <= nx < 2 and 0 <= ny < 3:
                        new_board = copy.deepcopy(node)
                        new_board[zx][zy], new_board[nx][ny] = new_board[nx][ny], new_board[zx][zy]
                        if to_string(new_board) not in visited:
                            q.append((new_board, num_moves + 1))

    return -1

