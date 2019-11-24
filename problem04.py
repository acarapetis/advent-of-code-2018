#!/usr/bin/python3

import sys
from collections import defaultdict

def charcount(string):
    counts = defaultdict(lambda: 0)
    for c in string:
        counts[c] += 1
    return counts

ids = [s.strip() for s in sys.stdin.readlines()]
def match(s1, s2):
    second = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if second:
                return False
            second = True
    return True

def same(s1, s2):
    r = ''
    for c1, c2 in zip(s1, s2):
        if c1 == c2:
            r += c1
    return r

for i1 in ids:
    for i2 in ids:
        if i1 > i2:
            continue
        if i1 != i2 and match(i1, i2):
            print(same(i1, i2))
