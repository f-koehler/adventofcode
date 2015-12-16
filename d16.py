#!/bin/env python3
import re

regex = re.compile(r"^Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)$")


def matching(gift, sue):
    for key, val in sue[1].items():
        if val != gift[key]:
            return False
    return True


def matching2(gift, sue):
    for key, val in sue[1].items():
        if key == "cats" or key == "trees":
            if val <= gift[key]:
                return False
        elif key == "pomeranians" or key == "goldfish":
            if val >= gift[key]:
                return False
        elif val != gift[key]:
            return False
    return True

if __name__ == "__main__":
    with open("d16.txt") as f:
        lines = f.read().splitlines()
    sues = []
    for l in lines:
        m = regex.match(l)
        sues.append((
            int(m.group(1)),
            {
                m.group(2): int(m.group(3)),
                m.group(4): int(m.group(5)),
                m.group(6): int(m.group(7))
            }
        ))
    gift = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }

    for sue in sues:
        if matching(gift, sue):
            print(sue[0])
            break

    for sue in sues:
        if matching2(gift, sue):
            print(sue[0])
            break
