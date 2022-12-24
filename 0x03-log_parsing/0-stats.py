#!/usr/bin/python3
"""This script reads stdin line by line computes metrics"""
import sys


if __name__ == "__main__":
    status_codes = {}
    total_size = 0
    count = 1

    def print_lines():
        """This method prints the state and its matches"""
        print("File size: {}".format(total_size))
        for status_code, matches in sorted(status_codes.items()):
            print("{}: {}".format(status_code, matches))

    def validation(line):
        """This method validate if the line has a correct format"""
        try:
            words = line.split()
            status_code = int(words[-2])

            if status_code in status_codes:
                status_codes[status_code] += 1
            elif status_code not in status_codes:
                status_codes[status_code] = 1
            return int(words[-1])
        except Exception:
            return 0

    try:
        for line in sys.stdin:
            total_size += validation(line)
            if count % 10 == 0:
                print_lines()
            count += 1
    except KeyboardInterrupt:
        print_lines()
        raise
    print_lines()
