#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""


def isWinner(x, nums):
    """
    is winner function
    determines the overall winner between Maria and Ben over multiple rounds.
    """

    if x <= 0 or nums is None or len(nums) == 0:
        return None

    ben_wins, maria_wins = 0, 0

    for n in nums:
        if n == 1:
            ben_wins += 1
        else:
            if play_game(n):
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None


def play_game(n):
    """
    The play_game function simulates one round of the game
    Players take turns removing a prime number and all its multiples.
    It returns True if Maria wins and False if Ben wins.
    """
    primes = [False, False] + [True] * (n - 1)
    current_player = 0

    for i in range(2, n + 1):
        if primes[i]:
            for j in range(i * 2, n + 1, i):
                primes[j] = False
            current_player = 1 - current_player

    return current_player == 1
