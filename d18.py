#!/bin/env python3

with open("d18.txt") as f:
    lines = f.read().splitlines()

dim_x = len(lines)
dim_y = len(lines[0])

lights = {
        (x, y) for y, l in enumerate(lines)
        for x, c in enumerate(l)
        if c == "#"
}


def active_neighbours(x, y):
    return sum(
            (x_n, y_n) in lights
            for x_n in (x-1, x, x+1)
            for y_n in (y-1, y, y+1)
            if (x_n, y_n) != (x, y)
    )


for i in range(100):
    lights = {
            (x, y)
            for x in range(dim_x)
            for y in range(dim_y)
            if (((x, y) in lights) and (2 <= active_neighbours(x, y) <= 3)) or
            (((x, y) not in lights) and (active_neighbours(x, y) == 3))
    }
print(len(lights))


# part 2
corners = {(0, 0), (0, dim_y-1), (dim_x-1, 0), (dim_x-1, dim_y-1)}
lights = corners | {
        (x, y) for y, l in enumerate(lines)
        for x, c in enumerate(l)
        if c == "#"
}


def active_neighbours(x, y):
    return sum(
            (x_n, y_n) in lights
            for x_n in (x-1, x, x+1)
            for y_n in (y-1, y, y+1)
            if (x_n, y_n) != (x, y)
    )


for i in range(100):
    lights = corners | {
            (x, y)
            for x in range(dim_x)
            for y in range(dim_y)
            if (((x, y) in lights) and (2 <= active_neighbours(x, y) <= 3)) or
            (((x, y) not in lights) and (active_neighbours(x, y) == 3))
    }
print(len(lights))
