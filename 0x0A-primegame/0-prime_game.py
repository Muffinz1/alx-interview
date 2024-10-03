#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""
def isWinner(x, nums):
    if x <= 0 or nums is None or x != len(nums):
        return None
    ben_wins, maria_wins = win_game(nums)
    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return None


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def win_game(nums):
    ben = 0
    maria = 0
    for n in nums:
        prime_count = sum(1 for i in range(n + 1) if prime(i))
        if prime_count % 2 == 0:
            ben += 1
        else:
            maria += 1
    return ben, maria

