#!/bin/env python3
import json


def sum_numbers(data):
    if type(data) == int:
        return data
    if type(data) == list:
        return sum([sum_numbers(d) for d in data])
    if type(data) == dict:
        return sum_numbers(list(data.values()))
    return 0


def sum_numbers2(data):
    if type(data) == int:
        return data
    if type(data) == list:
        return sum([sum_numbers2(d) for d in data])
    if type(data) == dict:
        if "red" in data.values():
            return 0
        return sum_numbers2(list(data.values()))
    return 0


if __name__ == "__main__":
    with open("d12.txt") as f:
        data = json.load(f)
    print(sum_numbers(data))
    print(sum_numbers2(data))
