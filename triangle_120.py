from typing import List

def triangle_path_sum(triangle: List[List[int]]) -> int:
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] = triangle[i][j] + min(triangle[i + 1][j], triangle[i + 1][j + 1])
    
    return triangle[0][0]