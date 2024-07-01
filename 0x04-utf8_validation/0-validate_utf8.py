#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    Method to determine if a given dataset is a valid UTF-8 encoding.
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
