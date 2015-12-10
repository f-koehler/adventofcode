#!/bin/env python3

import re

regex = re.compile(r"(\\x[\da-f]{2})")


def literal_length(literal):
    return len(literal)


def memory_length(literal):
    literal = literal.strip("\"")
    literal = literal.replace("\\\\", "\\")
    literal = literal.replace("\\\"", "\"")
    literal = regex.sub("X", literal)
    return len(literal)


def escaped_length(literal):
    literal = literal.replace("\\", "\\\\")
    literal = literal.replace("\"", "\\\"")
    literal = "\""+literal+"\""
    return len(literal)

if __name__ == "__main__":
    with open("d08.txt") as f:
        literals = f.read().splitlines()

    lit = 0
    mem = 0
    esc = 0
    for literal in literals:
        lit += literal_length(literal)
        mem += memory_length(literal)
        esc += escaped_length(literal)
    print(lit-mem)
    print(esc-lit)
