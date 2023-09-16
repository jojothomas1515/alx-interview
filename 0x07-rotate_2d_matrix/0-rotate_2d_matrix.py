#!/usr/bin/python3
"""Rotate matrix."""


def rotate_2d_matrix(matrix):
    """Rotate 2d matrix."""
    size = len(matrix)

    new_matrix = [[0 for _ in range(size)] for _ in range(size)]

    for i, li in enumerate(matrix):
        for j, v in enumerate(li):
            new_matrix[j][(size - 1) - i] = v

    matrix.clear()
    matrix.extend(new_matrix)
