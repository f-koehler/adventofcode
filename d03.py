#!/bin/env python3
if __name__ == "__main__":
    x = 0
    y = 0
    visited = dict()
    visited[0] = [0]
    num_visited = 1

    with open("d03.txt") as f:
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

    visited = dict()
    visited[0] = [0]
    num_visited = 1
    robo = False
    x_santa = 0
    y_santa = 0
    x_robo = 0
    y_robo = 0

    for cmd in commands:
        if not robo:
            if cmd == "^":
                y_santa += 1
            elif cmd == ">":
                x_santa += 1
            elif cmd == "v":
                y_santa -= 1
            else:
                x_santa -= 1

            if x_santa not in visited:
                visited[x_santa] = [y_santa]
                num_visited += 1
                robo = not robo
                continue
            elif y_santa not in visited[x_santa]:
                visited[x_santa].append(y_santa)
                num_visited += 1
                robo = not robo
                continue
            robo = not robo
        else:
            if cmd == "^":
                y_robo += 1
            elif cmd == ">":
                x_robo += 1
            elif cmd == "v":
                y_robo -= 1
            else:
                x_robo -= 1

            if x_robo not in visited:
                visited[x_robo] = [y_robo]
                num_visited += 1
                robo = not robo
                continue
            elif y_robo not in visited[x_robo]:
                visited[x_robo].append(y_robo)
                num_visited += 1
                robo = not robo
                continue
            robo = not robo
    print(num_visited)
