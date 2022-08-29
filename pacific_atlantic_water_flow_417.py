from typing import List 

def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    rows = len(heights)
    cols = len(heights[0])
    pacific = set()
    atlantic = set()
    result = []


    def dfs(coord, visited, prev):
        x = coord[0]
        y = coord[1]

        if (coord in visited
                or x < 0
                or y < 0
                or x == rows
                or y == cols
                or heights[x][y] < prev):
            return

        val = heights[x][y]
        visited.add(coord)
        dfs((x + 1, y), visited, val)
        dfs((x - 1, y), visited, val)
        dfs((x, y + 1), visited, val)
        dfs((x, y - 1), visited, val)


    for j in range(cols):
        dfs((0, j), pacific, heights[0][j])
        dfs((rows - 1, j), atlantic, heights[rows - 1][j])
        
    for i in range(rows):
        dfs((i, 0), pacific, heights[i][0])
        dfs((i, cols - 1), atlantic, heights[i][cols - 1])

    for x in range(rows):
        for y in range(cols):
            if (x, y) in pacific and (x, y) in atlantic:
                result.append([x, y])

    return result

