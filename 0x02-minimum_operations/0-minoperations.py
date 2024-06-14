#!/usr/bin/python3
"""
A module that helps in
calculating the minimum number of operations
in order to achieve a given number of characters
"""


def minOperations(n: int) -> int:
    """
    Minimum Operations needed to get
    the number of H characters
    """
    if n <= 1:
        return 0
    oper = 0
    div = 2

    while n > 1:
        while n % div == 0:
            oper += div
            n //= div
        div += 1
    return oper
