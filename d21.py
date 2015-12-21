#!/bin/env python3
import re
import itertools

with open("d21.txt") as f:
    regex = re.compile(r"^Hit Points: (\d+)\nDamage: (\d+)\nArmor: (\d+)$")
    string = f.read()
    m = regex.match(string)
    boss = (int(m.group(1)), int(m.group(2)), int(m.group(3)))

weapons = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0),
]

armors = [
    (0, 0, 0),
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
]

rings = [
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
]


def simulate_fight(boss, dmg, arm):
    player_dmg = dmg-boss[2]
    player_life = 100
    boss_dmg = boss[1]-arm
    boss_life = boss[0]

    if player_dmg < 1:
        player_dmg = 1
    if boss_dmg < 1:
        boss_dmg = 1

    while True:
        boss_life -= player_dmg
        if boss_life <= 0:
            return True
        player_life -= boss_dmg
        if player_life <= 0:
            return False


min_cost = 1e200
max_cost = 0
for num_rings in [0, 1, 2]:
    for ring_combo in itertools.combinations(rings, num_rings):
        for weapon in weapons:
            for armor in armors:
                dmg = weapon[1]
                arm = armor[2]
                cost = weapon[0]+armor[0]
                for ring in ring_combo:
                    dmg += ring[1]
                    arm += ring[2]
                    cost += ring[0]
                if simulate_fight(boss, dmg, arm):
                    if cost < min_cost:
                        min_cost = cost
                else:
                    if cost > max_cost:
                        max_cost = cost

print(min_cost)
print(max_cost)
