#!/bin/env python3
if __name__ == "__main__":
    with open("d1.txt") as f:
        innstruction = "".join(f.readlines())
        floor = 0
        i = 0
        entered_basement = False
        for c in innstruction:
            if c == '(':
                floor += 1
            else:
                floor -= 1
                if not entered_basement and floor == -1:
                    entering_position = i
                    entered_basement = True
            i += 1
        print(floor)
        print(entering_position+1)
