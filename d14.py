#!/bin/env python3
import re
import operator

def distance(reindeer, time):
    fly_speed = reindeer[1]
    fly_time = reindeer[2]
    rest_time = reindeer[3]
    resting = False
    t = 0
    dist = 0
    while t < time:
        if resting:
            t += rest_time
            resting = False
        else:
            if t+fly_time < time:
                dist += fly_speed*fly_time
                t += fly_time
                resting = True
            else:
                dist += fly_speed*(time-t)
                t += time-t
    return dist

if __name__ == "__main__":
    regex = re.compile(r"^(\w+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds\.$")
    with open("d14.txt") as f:
        lines = f.read().splitlines()

    reindeer = []
    for l in lines:
        m = regex.match(l)
        reindeer.append((m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))))

    print(max([distance(r, 2503) for r in reindeer]))

    points = dict()
    for r in reindeer:
        points[r[0]] = 0
    for t in range(1, 2503):
        m = max([distance(r, t) for r in reindeer])
        for r in reindeer:
            if distance(r, t) == m:
                points[r[0]] += 1
    print(max(points.values()))
