#!/usr/bin/env python3

"""
Interview question solution module.
"""


def makeChange(coins, total):
    """Making changes.

    Args:
        coins (list): list of coins that can be used to makes changes.
        total (int): the amount to meet up with change.
    Returns:
        (int): The number of coins or -1 if the change cannot make that value.
        if total is 0 or less than zero return 0.
    """

    if total <= 0:
        return 0
    agg = 0
    count = 0

    while agg < total:
        coinss = coins
        m = -1
        for i in coinss:
            if (max(coinss) + agg) > total:
                coinss = list(filter(lambda x: x != max(coinss), coinss))
                continue
            m = max(coinss)

        if m == -1:
            return -1
        agg += m
        count += 1
    return count
