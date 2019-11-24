#!/usr/bin/python3
import sys

def react(polymer):
    L = 0
    while len(polymer) != L:
        L = len(polymer)
        for i in range(L - 1):
            a, b = polymer[i:i+2]
            if b is not False and a is not False and a != b and a.lower() == b.lower():
                polymer[i:i+2] = False, False
        polymer = list(filter(bool, polymer))
    return polymer

polymer = list(sys.stdin.read().strip())
print(len(react(polymer)))
