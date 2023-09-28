#!/usr/bin/python3
"""Interview question solution for island perimeter."""


def check_perimeter(grid, i, j):
    """ island perimeter helper function. """
    res = 0
    try:
        if i == 0 or not grid[i-1][j]:
            res += 1
    except Exception as e:
        res += 1
    try:
        if not grid[i+1][j] or i == len(grid) - 1:
            res += 1
    except Exception as e:
        res += 1

    try:
        if not grid[i][j+1] or j == len(grid[i]) - 1:
            res += 1
    except Exception as e:
        res += 1

    try:
        if not grid[i][j - 1] or j == 0:
            res += 1
    except Exception as e:
        res += 1

    return res


def island_perimeter(grid):
    """Calculate the island representing grid.

    Args:
        grid: NxN matrix.
    Returns: the perimeter
    """
    res = 0
    for idx, val in enumerate(grid):
        for j, vl in enumerate(val):
            if vl == 1:
                res += check_perimeter(grid, idx, j)
    return res
