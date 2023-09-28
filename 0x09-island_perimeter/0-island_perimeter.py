#!/usr/bin/python3
"""Interview question solution for island perimeter."""


def island_perimeter(grid):
    """Calculate the island representing grid.

    Args:
        grid: NxN matrix.
    Returns: the perimeter
    """
    count = 0
    col_len = len(grid)

    for i, row in enumerate(grid):
        row_len = len(row)
        for j, v in enumerate(row):
            cc = 0
            if v == 1:

                if not ((j + 1) >= row_len):
                    if grid[i][j + 1] == 0:
                        count += 1
                        cc += 1
                if not ((j - 1) < 0):
                    if grid[i][j - 1] == 0:
                        count += 1
                        cc += 1
                if not ((i + 1) >= col_len):
                    if grid[i + 1][j] == 0:
                        count += 1
                        cc += 1
                if not ((i - 1) < 0):
                    if grid[i - 1][j] == 0:
                        count += 1
                        cc += 1

                if cc == 4:
                    count -= 4

    return count
