#!/bin/env python3
import re
import string

all_letters = string.ascii_lowercase
forbidden_letters = "iol"
letters = [c for c in all_letters if c not in forbidden_letters]
sequences = [all_letters[i]+all_letters[i+1]+all_letters[i+2] for i in range(len(all_letters)-2)]
sequences = [seq for seq in sequences if not any([f in seq for f in forbidden_letters])]
regex = re.compile(r"([a-z])\1")


def valid(pw):
    if not any([seq in pw for seq in sequences]):
        return False
    return len(set(regex.findall(pw))) >= 2


def increment(pw):
    if pw.endswith(letters[-1]):
        return increment(pw[:-1])+letters[0]
    else:
        return pw[:-1]+letters[letters.index(pw[-1])+1]


def next_password(pw):
    while True:
        pw = increment(pw)
        if valid(pw):
            return pw


if __name__ == "__main__":
    with open("d11.txt") as f:
        pw = f.read().strip()
    pw = next_password(pw)
    print(pw)
    pw = next_password(pw)
    print(pw)
