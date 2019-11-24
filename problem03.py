#!/usr/bin/python3

import sys
from collections import defaultdict

def charcount(string):
    counts = defaultdict(lambda: 0)
    for c in string:
        counts[c] += 1
    return counts

def hasexactly(n):
    return lambda s: n in charcount(s).values()

def checksum(strings):
    strings = [s.strip() for s in strings]
    return len(list(filter(hasexactly(2), strings))) * \
        len(list(filter(hasexactly(3), strings)))

print(checksum(sys.stdin.readlines()))
