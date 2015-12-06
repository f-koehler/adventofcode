#!/bin/env python3
if __name__ == "__main__":
    x = 0
    y = 0
    visited = dict()
    visited[0] = [0]
    num_visited = 1

    with open("d3.txt") as f:
        commands = f.read().strip()

    for cmd in commands:
        if cmd == "^":
            y += 1
        elif cmd == ">":
            x += 1
        elif cmd == "v":
            y -= 1
        else:
            x -= 1

        if x not in visited:
            visited[x] = [y]
            num_visited += 1
            continue
        elif y not in visited[x]:
            visited[x].append(y)
            num_visited += 1
            continue
    print(num_visited)
