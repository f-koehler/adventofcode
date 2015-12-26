#!/bin/env python3
from itertools import combinations
from functools import reduce
from operator import mul


def measure_entanglement(x):
    return reduce(mul, x, 1)


def is_splittable(packages, target, compartments):
    for length in range(1, len(packages)-compartments+1):
        for comb in (c for c in combinations(packages, length) if sum(c) == target):
            if compartments == 2 and sum(packages-set(comb)) == target:
                return True
            elif is_splittable(packages-set(comb), target, compartments-1):
                return True
    return False


def solve(packages, compartments):
    target = sum(packages) // compartments
    packages_set = set(packages)

    # generate all package combinations from length 1,...,length(items)
    for l in range(1, len(packages)):
        comb = combinations(packages, l)
        # remove combinations which do not sum up to the target sum
        # sort remaining combinations by entanglement
        groups = sorted(filter(lambda c: sum(c) == target, comb), key=measure_entanglement)
        for g in groups:
            # check if the set of the remaining is splittable to fit in the
            # remaining compartments
            # if yes we found the best balanced solution as we start with
            # 1,... packages in the passenger compartment and sorted by
            # entanglement
            if is_splittable(packages_set-set(g), target, compartments-1):
                return measure_entanglement(g)
    return None

with open("d24.txt") as f:
    lines = f.read().splitlines()
    packages = [int(l) for l in lines]

print(solve(packages, 3))
print(solve(packages, 4))
