#!/usr/bin/python3

def island_perimeter(grid):
    """Calculate the island representing grid.

    Args:
        grid: NxN matrix.
    Returns: the perimeter
    """
    count = 0
    lenght = len(grid)

    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v == 1:

                if not ((j + 1) >= lenght):
                    if grid[i][j + 1] == 0:
                        count += 1
                if not ((j - 1) < 0):
                    if grid[i][j - 1] == 0:
                        count += 1
                if not ((i + 1) >= lenght):
                    if grid[i + 1][j] == 0:
                        count += 1
                if not ((i - 1) < 0):
                    if grid[i - 1][j] == 0:
                        count += 1

    return count
