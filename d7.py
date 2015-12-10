#!/bin/env python3
import re


gate_map = dict()


def evaluate(output):
    input1 = gate_map[output][1]
    if isinstance(input1, str):
        if input1.isnumeric():
            input1 = int(input1)
        else:
            input1 = int(evaluate(input1))
    gate_map[output][1] = input1

    typ = gate_map[output][0]
    if typ == "set":
        return input1
    elif typ == "not":
        return ~input1

    input2 = gate_map[output][2]
    if isinstance(input2, str):
        if input2.isnumeric():
            input2 = int(input2)
        else:
            input2 = int(evaluate(input2))
    gate_map[output][2] = input2

    if typ == "and":
        return str(input1 & input2)
    elif typ == "or":
        return str(input1 | input2)
    elif typ == "lshift":
        return str(input1 << input2)
    else:
        return str(input1 >> input2)

if __name__ == "__main__":
    re_set = re.compile(r"^(?P<in>[a-z]+|\d+) -> (?P<out>[a-z]+)$")
    re_not = re.compile(r"^NOT (?P<in>[a-z]+|\d+) -> (?P<out>[a-z]+)$")
    re_bin = re.compile(r"^(?P<in1>[a-z]+|\d+) (?P<op>AND|OR|LSHIFT|RSHIFT) (?P<in2>[a-z]+|\d+) -> (?P<out>[a-z]+)$")

    with open("d7.txt") as f:
        gates = f.read().splitlines()

    for gate in gates:
        m = re_set.match(gate)
        if m:
            d = m.groupdict()
            gate_map[d["out"]] = ["set", d["in"], None]
            continue

        m = re_not.match(gate)
        if m:
            d = m.groupdict()
            gate_map[d["out"]] = ["not", d["in"], None]
            continue

        m = re_bin.match(gate)
        if m:
            d = m.groupdict()
            gate_map[d["out"]] = [d["op"].lower(), d["in1"], d["in2"]]

    print(evaluate("a"))
