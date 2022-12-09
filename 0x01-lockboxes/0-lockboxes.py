#!/usr/bin/python3
"""Defining my function canUnlockAll"""


def canUnlockAll(boxes):
    """This function determines if all the boxes can be opened"""
    keys = [0]
    size = len(boxes)

    for key in keys:
        for box in boxes[key]:
            if box not in keys:
                if box < size:
                    keys.append(box)
    if size == len(keys):
        return True
    return False
