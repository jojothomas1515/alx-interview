#!/usr/bin/python3
"""Prime Game module."""


def isWinner(x, nums):
    """Calculate for the winner of most rounds
    Args:
        x (int): number of rounds
        nums (list[int]): list of int
    """

    winner = {"Maria": 0, "Ben": 0}

    for i in range(x):
        size = nums[i]
        if size == 1:
            break
        p_list = [j + 1 for j in range(size)]

        turn = 1

        while True:
            if turn == 0:
                turn == 1
            else:
                turn = 0
            end_turn = 0
            for n in p_list:
                if isPrime(n):
                    # removed prime number and it multiples

                    p_list = list(filter(lambda x: (x % n) != 0, p_list))
                    end_turn = 1
                    break
            if end_turn == 1:
                continue

            if turn == 1:
                winner["Maria"] = winner["Maria"] + 1
            else:
                winner["Ben"] = winner["Ben"] + 1

            break

    if winner["Ben"] > winner["Maria"]:
        return "Ben"
    return "Maria"


def isPrime(n):
    """Check if a number is prime
    Args:
        n (int): number to check
    """

    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
