#!/bin/env python3
def num_vowels(word):
    return word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u")


def bad_string(word):
    return "ab" in word or "cd" in word or "pq" in word or "xy" in word


def double_char(word):
    for i in range(0, len(word)-1):
        if word[i] == word[i+1]:
            return True
    return False


def nice_word(word):
    if not double_char(word):
        return False
    if bad_string(word):
        return False
    return num_vowels(word) >= 3


if __name__ == "__main__":
    with open("d5.txt") as f:
        words = f.read().splitlines()
    print(sum(1 for w in words if nice_word(w)))
