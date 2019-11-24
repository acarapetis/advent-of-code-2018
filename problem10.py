#!/usr/bin/python3
import sys
from string import ascii_lowercase

# Slow as ass. Should re-implement with linked list.
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

polymer = sys.stdin.read().strip()

def remove_and_react(char):
    return len(react(list(polymer
                          .replace(char.lower(), '')
                          .replace(char.upper(), ''))))

print(min(map(remove_and_react, ascii_lowercase)))
