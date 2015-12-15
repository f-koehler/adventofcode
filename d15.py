#!/bin/env python3
import re

regex = re.compile(r"^(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)$")
ingredients = []


def score(amounts):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0
    for i in range(0, len(ingredients)):
        capacity += ingredients[i][0]*amounts[i]
        durability += ingredients[i][1]*amounts[i]
        flavor += ingredients[i][2]*amounts[i]
        texture += ingredients[i][3]*amounts[i]
        calories += ingredients[i][4]*amounts[i]
    if capacity <= 0 or durability <= 0 or flavor <= 0 or texture <= 0:
        return (0, calories)
    return (capacity*durability*flavor*texture, calories)


def maximize():
    max_score = 0
    for i in range(0, 101):
        for j in range(0, 101-i):
            for k in range(0, 101-i-j):
                l = 100-i-j-k
                s = score((i, j, k, l))[0]
                if s > max_score:
                    max_score = s
    return max_score


def maximize2():
    max_score = 0
    for i in range(0, 101):
        for j in range(0, 101-i):
            for k in range(0, 101-i-j):
                l = 100-i-j-k
                s, c = score((i, j, k, l))
                if not c == 500:
                    continue
                if s > max_score:
                    max_score = s
    return max_score

if __name__ == "__main__":
    with open("d15.txt") as f:
        lines = f.read().splitlines()
    for l in lines:
        m = regex.match(l)
        ingredients.append(
            (
                int(m.group(2)), int(m.group(3)),
                int(m.group(4)), int(m.group(5)),
                int(m.group(6))
            )
        )
    print(maximize())
    print(maximize2())
