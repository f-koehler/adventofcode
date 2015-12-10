#!/bin/env python3
def num_vowels(word):
    return sum(word.count(c) for c in "aeiou")


def bad_string(word):
    return "ab" in word or "cd" in word or "pq" in word or "xy" in word


def double_char(word):
    for i in range(0, len(word)-1):
        if word[i] == word[i+1]:
            return True
    return False


def repetition(word):
    for i in range(0, len(word)-2):
        if word[i] == word[i+2]:
            return True
    return False


def non_overlapping(word):
    for i in range(len(word)-1):
        pair = word[i:i+2]
        right = word[i+2:]
        if pair in right:
            return True
    return False


def nice_word(word):
    if not double_char(word):
        return False
    if bad_string(word):
        return False
    return num_vowels(word) >= 3


def nice_word2(word):
    if not repetition(word):
        return False
    return non_overlapping(word)


if __name__ == "__main__":
    with open("d05.txt") as f:
        words = f.read().splitlines()
    print(sum(1 for w in words if nice_word(w)))
    print(sum(1 for w in words if nice_word2(w)))
