from typing import List


def countSquaresBruteForce(matrix: List[List[int]]) -> int:
    max_square_size = min(len(matrix), len(matrix[0]))
    num_squares = 0

    def check_square(x, y, square_size):
        all_ones = True
        for i in range(x, x + square_size):
            for j in range(y, y + square_size):
                if matrix[i][j] != 1:
                    all_ones = False
                    break
        return all_ones


    for square_size in range(max_square_size, 0, -1):

        for x in range(len(matrix) - square_size + 1):
            for y in range(len(matrix[0]) - square_size + 1):
                if check_square(x, y, square_size):
                    num_squares += 1

    return num_squares


def countSquaresDP(matrix: List[List[int]]) -> int:
    num_squares = 0
    dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

            num_squares += dp[i][j]

    return num_squares

