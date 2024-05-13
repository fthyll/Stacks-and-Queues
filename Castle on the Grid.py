#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

def minimumMoves(grid, startX, startY, goalX, goalY):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    queue = [(startX, startY, 0)]  # (x, y, moves)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # possible movements: down, up, right, left

    while queue:
        x, y, moves = queue.pop(0)
        if x == goalX and y == goalY:
            return moves
        visited[x][y] = True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == '.':
                if not visited[nx][ny]:
                    queue.append((nx, ny, moves + 1))
                    visited[nx][ny] = True
                nx += dx
                ny += dy

    return -1  # If goal is unreachable

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
