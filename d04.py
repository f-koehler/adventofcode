#!/bin/env python3
import hashlib

if __name__ == "__main__":
    with open("d04.txt") as f:
        secret = f.read().strip()
    num = 1
    while True:
        digest = hashlib.md5((secret+str(num)).encode()).hexdigest()
        if digest[0:5] == "00000":
            print(num)
            break
        num += 1
    num = 1
    while True:
        digest = hashlib.md5((secret+str(num)).encode()).hexdigest()
        if digest[0:6] == "000000":
            print(num)
            break
        num += 1
