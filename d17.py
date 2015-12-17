#!/bin/env python3
import itertools


def combinations(containers, target):
    comb = [1]+[0]*(target)
    for c in containers:
        for nxt in range(target, c-1, -1):
            comb[nxt] += comb[nxt-c]
    return comb[target]


def maximal_spare_combinations(containers, target):
    comb = 0
    for length in range(1, len(containers)+1):
        for c in itertools.combinations(containers, length):
            if sum(c) == 150:
                comb += 1
        if comb > 0:
            break
    return comb

if __name__ == "__main__":
    with open("d17.txt") as f:
        lines = f.read().splitlines()
    containers = [int(l) for l in lines]
    print(combinations(containers, 150))
    print(maximal_spare_combinations(containers, 150))
