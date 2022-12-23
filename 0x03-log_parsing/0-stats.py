#!/usr/bin/python3
"""This script reads stdin line by line computes metrics"""
import sys

status_codes = {}
total_size = 0
count = 0

try:
    for line in sys.stdin:
        words = line.split(" ")
        if len(words) != 9:
            continue

        count += 1
        total_size += int(words[8])

        status_code = words[7]
        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1

        if count % 10 == 0:
            print("File size: {}".format(total_size))
            for status_code, count in sorted(status_codes.items()):
                print("{}: {}".format(status_code, count))

except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for status_code, count in sorted(status_codes.items()):
        print("{}: {}".format(status_code, count))

