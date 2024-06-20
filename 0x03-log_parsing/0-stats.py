#!/usr/bin/python3
import sys
import re

def output(log):
    """
    Displays the file size and the frequency of each status
    """
    print(f"File size: {log['file_size']}")
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code] > 0:
            print(f"{code}: {log['code_frequency'][code]}")

def process_line(line, log):
    """
    process a line and updates the statistics
    """
    match = regex.fullmatch(line)
    if match:
        code = match.group(1)
        file_size = int(match.group(2))
        log["file_size"] += file_size
        if code in log["code_frequency"]:
            log["code_frequency"][code] += 1

if __name__ == "__main__":
    regex = re.compile(r'"GET /projects/260 HTTP/1.1" (\d{3}) (\d+)')

    line_count = 0
    log = {
        "file_size": 0,
        "code_frequency": {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
    }

    try:
        for line in sys.stdin:
            line = line.strip()
            process_line(line, log)
            line_count += 1
            if line_count % 10 == 0:
                output(log)
    finally:
        output(log)
