#!/bin/env python3
if __name__ == "__main__":
    with open("d1.txt") as f:
        innstruction = "".join(f.readlines())
        floor = 0
        for c in innstruction:
            if c == '(':
                floor += 1
            else:
                floor -= 1
        print(floor)
