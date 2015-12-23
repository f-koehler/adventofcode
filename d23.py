#!/bin/env python3
import re

regex = re.compile(r"^(\w+) (\w+|[\+-]\d+)(?:, ([\+-]\d+))?$")

code = []
with open("d23.txt") as f:
    lines = f.read().splitlines()
    for l in lines:
        m = regex.match(l)
        instr = [m.group(1)]
        if instr[0] == "jmp":
            instr.append(int(m.group(2)))
            code.append(instr)
            continue
        instr.append(m.group(2))
        if instr[0] == "jie" or instr[0] == "jio":
            instr.append(int(m.group(3)))
        code.append(instr)

reg = {"a": 0, "b": 0}
codepos = 0


def instruction():
    global codepos
    instr = code[codepos]

    # print((reg["a"], reg["b"], codepos, instr))

    if instr[0] == "hlf":
        reg[instr[1]] = reg[instr[1]]/2
        codepos += 1
        return

    if instr[0] == "tpl":
        reg[instr[1]] = reg[instr[1]]*3
        codepos += 1
        return

    if instr[0] == "inc":
        reg[instr[1]] += 1
        codepos += 1
        return

    if instr[0] == "jmp":
        codepos += instr[1]
        return

    if instr[0] == "jie":
        if reg[instr[1]] % 2 == 0:
            codepos += instr[2]
        else:
            codepos += 1
        return

    if reg[instr[1]] == 1:
        codepos += instr[2]
    else:
        codepos += 1

while codepos < len(code):
    instruction()
print(reg["b"])

reg = {"a": 1, "b": 0}
codepos = 0
while codepos < len(code):
    instruction()
print(reg["b"])
