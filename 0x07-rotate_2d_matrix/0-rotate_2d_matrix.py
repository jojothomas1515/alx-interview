#!/usr/bin/python3
"""Rotate matrix."""

from typing import List


def rotate_2d_matrix(matrix: List[List[int]]):
    """Rotate 2d matrix."""
    size: int = len(matrix)

    new_matrix = [[0 for _ in range(size)] for _ in range(size)]

    for i, li in enumerate(matrix):
        for j, v in enumerate(li):
            new_matrix[j][(size - 1) - i] = v

    matrix.clear()
    matrix.extend(new_matrix)
