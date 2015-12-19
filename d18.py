#!/bin/env python3

with open("d18.txt") as f:
    state1 = f.read().splitlines()

for i in range(0, len(state1)):
    state1[i] = list(state1[i])

new_state = 2
dim_x = len(state1)
dim_y = len(state1[0])
state2 = [["."]*(dim_y)]*(dim_x)


def light_active(x, y):
    if new_state == 1:
        return state2[x][y] == "#"
    return state1[x][y] == "#"


def turn_on(x, y):
    if new_state == 1:
        state1[x][y] = "#"
    else:
        state2[x][y] = "#"


def turn_off(x, y):
    if new_state == 1:
        state1[x][y] = "."
    else:
        state2[x][y] = "."


def active_neighbors(x, y):
    num = 0
    if x > 0:
        if light_active(x-1, y):
            num += 1
        if y > 0:
            if light_active(x-1, y-1):
                num += 1
        if y < dim_y-1:
            if light_active(x-1, y+1):
                num += 1
    if y > 0:
        if light_active(x, y-1):
            num += 1
    if x < dim_x-1:
        if light_active(x+1, y):
            num += 1
        if y > 0:
            if light_active(x+1, y-1):
                num += 1
        if y < dim_y-1:
            if light_active(x+1, y+1):
                num += 1
    if y < dim_y-1:
        if light_active(x, y+1):
            num += 1
    return num


def update_light(x, y):
    num = active_neighbors(x, y)
    if light_active(x, y):
        if num < 2 or num > 3:
            turn_off(x, y)
        else:
            turn_on(x, y)
    else:
        if num == 3:
            turn_on(x, y)
        else:
            turn_off(x, y)


def update():
    global new_state
    for x in range(0, dim_x):
        for y in range(0, dim_y):
            update_light(x, y)

    if new_state == 1:
        new_state = 2
    else:
        new_state = 1


def count_lights():
    num = 0
    for x in range(0, dim_x):
        for y in range(0, dim_y):
            if light_active(x, y):
                num += 1
    return num


def print_state(state_num):
    if state_num == 1:
        for l in state1:
            print("".join(l))
    else:
        for l in state2:
            print("".join(l))
    print()

print_state(1)
print_state(2)
update()
print_state(1)
print_state(2)
