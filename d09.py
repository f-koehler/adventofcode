#!/bin/env python3

import itertools
import re

if __name__ == "__main__":
    regex = re.compile(r"^(?P<from>\w+) to (?P<to>\w+) = (?P<dist>\d+)$")
    with open("d09.txt") as f:
        lines = f.read().splitlines()

    locations = []
    distances = dict()

    for l in lines:
        m = regex.match(l)
        f = m.groupdict()["from"]
        t = m.groupdict()["to"]
        d = int(m.groupdict()["dist"])
        if f not in locations:
            locations.append(f)
        if t not in locations:
            locations.append(t)
        if f not in distances:
            distances[f] = dict()
        if t not in distances:
            distances[t] = dict()
        distances[f][t] = d
        distances[t][f] = d

    min_route = 1e200
    max_route = 0
    for perm in itertools.permutations(locations):
        route = 0
        for i in range(1, len(locations)):
            route += distances[perm[i-1]][perm[i]]
        if route < min_route:
            min_route = route
        if route > max_route:
            max_route = route

    print(min_route)
    print(max_route)
