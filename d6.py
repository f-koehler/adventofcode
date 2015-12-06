#!/bin/env python3
import re

def part1():
    lights = []
    for x in range(0, 1000):
        lights.append([False for y in range(0, 1000)])
    regex = re.compile(r"^(?P<command>turn\son|turn\soff|toggle)\s(?P<x1>\d+),(?P<y1>\d+)\s+through\s+(?P<x2>\d+),(?P<y2>\d+)$")
    with open("d6.txt") as f:
        commands = f.read().splitlines()
    for cmd in commands:
        m = regex.match(cmd)
        grpdict = m.groupdict()
        c = grpdict["command"]
        x1 = int(grpdict["x1"])
        y1 = int(grpdict["y1"])
        x2 = int(grpdict["x2"])
        y2 = int(grpdict["y2"])
        if c == "turn on":
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    lights[x][y] = True
        elif c == "turn off":
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    lights[x][y] = False
        elif c == "toggle":
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    lights[x][y] = not lights[x][y]
    turned_on = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            if lights[x][y]:
                turned_on += 1
    print(turned_on)

def part2():
    lights = []
    for x in range(0, 1000):
        lights.append([0 for y in range(0, 1000)])
    regex = re.compile(r"^(?P<command>turn\son|turn\soff|toggle)\s(?P<x1>\d+),(?P<y1>\d+)\s+through\s+(?P<x2>\d+),(?P<y2>\d+)$")
    with open("d6.txt") as f:
        commands = f.read().splitlines()
    for cmd in commands:
        m = regex.match(cmd)
        grpdict = m.groupdict()
        c = grpdict["command"]
        x1 = int(grpdict["x1"])
        y1 = int(grpdict["y1"])
        x2 = int(grpdict["x2"])
        y2 = int(grpdict["y2"])
        if c == "turn on":
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    lights[x][y] += 1
        elif c == "turn off":
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    lights[x][y] -= 1
                    if lights[x][y] < 0:
                        lights[x][y] = 0
        elif c == "toggle":
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    lights[x][y] += 2
    brightness = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            brightness += lights[x][y]
    print(brightness)

if __name__ == "__main__":
    part1()
    part2()
