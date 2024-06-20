#!/usr/bin/python3
"""
Module for log parser
"""
import sys

def print_statistics(status_code_counts, total_size):
    """
    prints the file size and status code counts.
    """
    print("File size: {}".format(total_size))
    for status_code in sorted(status_code_counts):
        count = status_code_counts[status_code]
        if count > 0:
            print("{}: {}".format(status_code, count))
total_file_size = 0
line_counter = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) > 2:
            file_size_str = parts[-1]
            status_code = parts[-2]
            try:
                file_size = int(file_size_str)
                total_file_size += file_size
                line_counter += 1

                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1

                if line_counter == 10:
                    print_statistics(status_code_counts, total_file_size)
                    line_counter = 0

            except ValueError:
                continue

finally:
    if line_counter > 0:
        print_statistics(status_code_counts, total_file_size)
