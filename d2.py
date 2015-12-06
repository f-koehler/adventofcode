#!/bin/env python3
def gift_area(l, w, h):
    side_a = l*w
    side_b = w*h
    side_c = l*h
    return 2*side_a+2*side_b+2*side_c+min((side_a, side_b, side_c))

def gift_ribbon(l, w, h):
    side_a = 2*l+2*w
    side_b = 2*w+2*h
    side_c = 2*l+2*h
    ribbon = min((side_a, side_b, side_c))
    ribbon += l*w*h
    return ribbon

if __name__ == "__main__":
    with open("d2.txt") as f:
        lines = f.readlines()
    gifts = []
    for l in lines:
        fields = l.split("x")
        gifts.append([int(f) for f in fields])
    area = 0
    ribbon = 0
    for g in gifts:
        area += gift_area(g[0], g[1], g[2])
        ribbon += gift_ribbon(g[0], g[1], g[2])
    print(area)
    print(ribbon)
