#!/usr/bin/python3
""" defining a makechange function to deal with coins and change"""


def makeChange(coins, total):
    """
    checks the change for everything,
    sorts the coins backward in order to use the biggest coins first
    determines the fewest number of coins needed to meet a given
    amount total.
    """
    if total <= 0:
        return 0
    if not coins:
        return -1
    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        if coin <= total:
            num_coins += total // coin
            total %= coin
            if total == 0:
                return num_coins
    return -1
