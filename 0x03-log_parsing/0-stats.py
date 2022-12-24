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

    try:
        for line in sys.stdin:
            try:
                words = line.split()
                total_size += int(words[-1])
                status_code = int(words[-2])

                if status_code in status_codes:
                    status_codes[status_code] += 1
                else:
                    status_codes[status_code] = 1
            except Exception:
                pass

            if count % 10 == 0:
                print_lines()
            count += 1
    except KeyboardInterrupt:
        print_lines()
        raise
    print_lines()
