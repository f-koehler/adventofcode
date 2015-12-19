#!/bin/env python3
import re

regex = re.compile(r"^(\w+) => (\w+)$")

with open("d19.txt") as f:
    lines = f.read().splitlines()

start = lines[-1]
destination = start
lines = lines[:-2]
replacements = []
for l in lines:
    m = regex.match(l)
    replacements.append((m.group(1), m.group(2)))

molecules = set()
for r in replacements:
    for m in re.finditer(r[0], start):
        molecules.add(start[:m.start()]+r[1]+start[m.end():])

print(len(molecules))


count = 0
cur_string = start
while cur_string != "e":
    for r in replacements:
        if r[1] in cur_string:
            cur_string = cur_string.replace(r[1], r[0], 1)
            count += 1

print(count)
