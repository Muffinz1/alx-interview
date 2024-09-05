#!/usr/bin/python3
"""UTF-8 Validation function intialization"""


def validUTF8(data):
    """
    Method to determine if a given dataset is a valid UTF-8 encoding.
    1-byte character: 0xxxxxxx
    2-byte character: 110xxxxx 10xxxxxx
    3-byte character: 1110xxxx 10xxxxxx 10xxxxxx
    4-byte character: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
    while meeting the coniditions of the bytes usage.
    The Function Time Complexity is O(n)
    """
    num_bytes = 0

    byte1 = 1 << 7
    byte2 = 1 << 6

    for byte in data:
        bytechecker = 1 << 7

        if num_bytes == 0:
            while bytechecker & byte:
                num_bytes += 1
                bytechecker >>= 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            if not (byte & byte1 and not (byte & byte2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
