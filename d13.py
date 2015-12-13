#!/bin/env python3
import itertools
import re

if __name__ == "__main__":
    regex = re.compile(r"^(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\.$")
    with open("d13.txt") as f:
        lines = f.read().splitlines()

    names = []
    relations = dict()
    for l in lines:
        m = regex.match(l)
        name1 = m.group(1)
        name2 = m.group(4)
        if name1 not in relations:
            relations[name1] = dict()
        if not name1 in names:
            names.append(name1)
        change = int(m.group(3))
        if m.group(2) == "lose":
            change *= -1
        relations[name1][name2] = change

    max_total = 0
    for perm in itertools.permutations(names):
        total = 0
        for i in range(0, len(names)):
            total += relations[perm[i]][perm[(i+1) % len(names)]]
            total += relations[perm[i]][perm[i-1]]
        max_total = max(total, max_total)
    print(max_total)

    relations["Me"] = dict()
    for name in names:
        relations[name]["Me"] = 0
        relations["Me"][name] = 0
    names.append("Me")

    max_total = 0
    for perm in itertools.permutations(names):
        total = 0
        for i in range(0, len(names)):
            total += relations[perm[i]][perm[(i+1) % len(names)]]
            total += relations[perm[i]][perm[i-1]]
        max_total = max(total, max_total)
    print(max_total)
