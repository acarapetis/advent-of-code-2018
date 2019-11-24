#!/usr/bin/python3

import sys

def loop(xs):
    xs = list(xs)
    while True:
        for x in xs:
            yield x

deltas = loop(map(int, sys.stdin.readlines()))

def firstdup():
    x = 0
    seen = set()
    for d in deltas:
        seen.add(x)
        x += d
        if x in seen:
            return x

print(firstdup())
