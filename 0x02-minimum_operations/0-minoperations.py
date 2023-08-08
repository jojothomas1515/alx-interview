#!/usr/bin/python3
"""
Minimum operations
"""


def minOperations(n):
    """
    Min ops.
    """
    H = 1
    inc = 1
    opc_count = 1
    while True:
        if H == n:
            # return operation count if the number of h is same as n
            return opc_count
        elif H > n:
            # return 0 if h is greater than n , which means it nor feasible
            return 0
        # copy all and paste if condition is true
        if n % H == 0 and H != 1:
            inc = H
            H += inc
            opc_count += 2
        # paste H if false
        else:
            H += inc
            opc_count += 1
