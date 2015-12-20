#!/bin/env python3

# bruteforce is still faster on this scale

N = 29000000
n = N // 10

house = [1]*(n+1)
for i in range(2, n+1):
    for j in range(i, n, i):
        house[j] += i

for i, h in enumerate(house):
    if h >= n:
        print(i)
        break

house = [0]+[11]*(50)+[0]*(n-50)
for i in range(2, n+1):
    for j in range(i, 51*i, i):
        if j >= n:
            break
        house[j] += i*11

for i, h in enumerate(house):
    if h >= N:
        print(i)
        break
