#!/bin/env python3
import itertools


def look_and_say(sequence):
    new_sequence = ""
    for element, grp in itertools.groupby(sequence):
        new_sequence += str(len(list(grp))) + element
    return new_sequence

if __name__ == "__main__":
    with open("d10.txt") as f:
        sequence = f.read().strip()
    for i in range(0, 40):
        sequence = look_and_say(sequence)
    print(len(sequence))
    for i in range(0, 10):
        sequence = look_and_say(sequence)
    print(len(sequence))
