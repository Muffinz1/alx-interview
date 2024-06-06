#!/usr/bin/python3
"""
The module of the function that can whether unlock or not
"""


def canUnlockAll(boxes):
    """
    Defining a function that check if the boxes
    can be unlocked or not
    """
    unlocked = [False] * len(boxes)
    unlocked[0] = True
    keys = [0]
    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)
    return all(unlocked)
