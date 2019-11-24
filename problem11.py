#!/usr/bin/python3
import sys
import numpy as np

coords = [tuple(int(s.strip()) for s in l.strip().split(','))
          for l in sys.stdin.readlines()]
xmax = max(x for x, y in coords)
ymax = max(y for x, y in coords)
shape = (xmax + 1, ymax + 1)
R = max(*shape)

grid = np.zeros(shape, dtype=int)

# Seed grid with initial points
for i, c in enumerate(coords):
    grid[c] = i + 1

# Manhattan 1-neighbourhood
def neighbourhood(x, y):
    l = []
    for a, b in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        x1, y1  = x+a, y+b
        if x1 < 0 or x1 > xmax or y1 < 0 or y1 > ymax:
            continue
        l.append(grid[x+a, y+b])
    return l

def preview():
    for y in range(ymax+1):
        for x in range(xmax+1):
            v = grid[x, y]
            if v == -1:
                v = '.'
            elif v == 0:
                v = ' '
            else:
                v = chr(ord('a') - 1 + v)
            print(v, end='')
        print()
    print()

# Grow seed points gradually
for r in range(R):
    print(r, R)
    if np.all(grid != 0):
        break
    new = grid.copy()
    for x, y in np.ndindex(grid.shape):
        if new[x, y] != 0:
            continue
        surrounds = {v for v in neighbourhood(x, y)
                     if v != 0}
        if len(surrounds) == 1:
            new[x, y] = surrounds.pop()
        elif len(surrounds) > 1:
            new[x, y] = -1
    grid = new

boundary = np.concatenate((grid[0, :], grid[-1, :],
                           grid[:, 0], grid[:, -1]))
infinite = set(boundary)
vals, counts = np.unique(grid, return_counts=True)
count = max(c for v, c in zip(vals, counts)
            if v not in infinite)
print()
print(count)

#print(grid)
