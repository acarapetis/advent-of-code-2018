#!/usr/bin/python3
import sys
import re

class CyclicList(list):
    def normindex(self, index):
        if self:
            return index % len(self)
        return 0
    def __getitem__(self, index):
        return super().__getitem__(self.normindex(index))
    def __setitem__(self, index, x):
        return super().__setitem__(self.normindex(index), x)
    def insert(self, index, x):
        return super().insert(self.normindex(index), x)
    def pop(self, index=-1):
        return super().pop(self.normindex(index))

m = re.search(r'(\d+) players; last marble is worth (\d+) points', sys.stdin.read())
if not m:
    raise ValueError('Invalid input')

players, max_marble = (int(c) for c in m.groups())

if __name__ == '__main__':
    circle = CyclicList()
    scores = [0 for p in range(players)]
    current = 0
    player = 0
    for marble in range(max_marble+1):
        if marble and marble % 23 == 0:
            current = circle.normindex(current - 7)
            scores[player] += marble
            scores[player] += circle.pop(current)
        else:
            current = circle.normindex(current + 2)
            circle.insert(current, marble)
        player = (player + 1) % players
        if marble % 10000 == 0:
            print(marble)
    print(max(scores))
