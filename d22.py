#!/bin/env python3
from copy import deepcopy
import re

spells = [
    "Magic Missile",
    "Drain",
    "Shield",
    "Poison",
    "Recharge"
]

costs = {
    "Magic Missile": 53,
    "Drain": 73,
    "Shield": 113,
    "Poison": 173,
    "Recharge": 229
}

cast_damages = {
    "Magic Missile": 4,
    "Drain": 2,
    "Shield": 0,
    "Poison": 0,
    "Recharge": 0
}

effect_damages = {
    "Poison": 3
}

health_boosts = {
    "Magic Missile": 0,
    "Drain": 2,
    "Shield": 0,
    "Poison": 0,
    "Recharge": 0
}

armor_boosts = {
    "Shield": 7
}

mana_boosts = {
    "Recharge": 101
}

durations = {
    "Shield": 6,
    "Poison": 6,
    "Recharge": 5
}

memory = {}


class Player(object):
    hp = 50
    mana = 500
    armor = 0
    mana_spent = 0


class Boss(object):
    hp = 0
    dmg = 0


def apply_effects(player, boss, timers):
    if timers["Shield"] > 0:
        player.armor = armor_boosts["Shield"]
    else:
        player.armor = 0
    if timers["Poison"] > 0:
        boss.hp -= effect_damages["Poison"]
    if timers["Recharge"] > 0:
        player.mana += mana_boosts["Recharge"]
    for status in timers:
        timers[status] = max(0, timers[status]-1)
    return player, boss, timers


def turn_boss(player, boss, timers, hard_mode=False):
    player, boss, timers = apply_effects(player, boss, timers)
    if player.hp <= 0:
        return float('inf')
    if boss.hp <= 0:
        return player.mana_spent
    player.hp -= max(1, boss.dmg-player.armor)
    return turn_player(player, boss, timers, hard_mode)


def turn_player(player, boss, timers, hard_mode=False):
    memory_key = (
            player.hp, player.armor, player.mana, player.mana_spent,
            boss.hp, boss.dmg, tuple(timers), hard_mode
    )
    if memory_key in memory:
        return memory[memory_key]

    if hard_mode:
        player.hp -= 1

    player, boss, timers = apply_effects(player, boss, timers)
    if player.hp <= 0:
        return float('inf')
    if boss.hp <= 0:
        return player.mana_spent

    min_mana_spent = float('inf')

    for spell in spells:
        if player.mana >= costs[spell]:
            if spell in timers and timers[spell] > 0:
                continue
            new_timers = deepcopy(timers)
            if spell in new_timers:
                new_timers[spell] = durations[spell]
            p = deepcopy(player)
            b = deepcopy(boss)
            p.hp += health_boosts[spell]
            p.mana -= costs[spell]
            p.mana_spent += costs[spell]
            b.hp -= cast_damages[spell]
            result = turn_boss(p, b, new_timers, hard_mode)
            min_mana_spent = min(min_mana_spent, result)

    memory[memory_key] = min_mana_spent
    return min_mana_spent


player = Player()
boss = Boss()
timers = {
    "Shield": 0,
    "Poison": 0,
    "Recharge": 0
}

with open("d22.txt") as f:
    m = re.match(r"^Hit Points: (\d+)\nDamage: (\d+)$", f.read())
    boss.hp = int(m.group(1))
    boss.dmg = int(m.group(2))

print(turn_player(player, boss, timers, False))
print(turn_player(player, boss, timers, True))
