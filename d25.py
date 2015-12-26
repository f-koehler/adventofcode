#!/bin/env python3
import re


def powermod(a, b, n):
    r = 1
    while b > 0:
        if b & 1 == 1:
            r = r * a % n
        b //= 2
        a = a * a % n
    return r


def code_num(row, col):
    return (row+col-2)*(row+col-1)//2+col-1


def code(row, col, first=20151125, mul=252533, mod=33554393):
    num = code_num(row, col)
    return (powermod(mul, num, mod)*first) % mod


with open("d25.txt") as f:
    m = re.match(r"^[\w\s,\.]+?(\d+)[\w\s,\.]+?(\d+)\.$", f.read().strip())
    row = int(m.group(1))
    col = int(m.group(2))


print(code(row, col))
