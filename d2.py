#!/bin/env python3
def gift_area(l, w, h):
    side_a = l*w
    side_b = w*h
    side_c = l*h
    return 2*side_a+2*side_b+2*side_c+min((side_a, side_b, side_c))

if __name__ == "__main__":
    with open("d2.txt") as f:
        lines = f.readlines()
    gifts = []
    for l in lines:
        fields = l.split("x")
        gifts.append([int(f) for f in fields])
    area = 0
    for g in gifts:
        area += gift_area(g[0], g[1], g[2])
    print(area)
