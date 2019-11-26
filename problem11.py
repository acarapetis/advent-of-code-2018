#!/usr/bin/python3
import sys
import numpy as np

# This is super slow - for a "good" solution, either reimplement this approach
# in a compiled language, or redesign it to leverage numpy/scipy rather than
# loops.

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

# Grow seed points gradually
for r in range(R):
    if np.all(grid != 0):
        # we've determined the state of every tile; so we're done
        break
    new = grid.copy()
    for x, y in np.ndindex(grid.shape):
        if new[x, y] != 0:
            # tile has already been claimed
            continue
        surrounds = {v for v in neighbourhood(x, y)
                     if v != 0}
        # If there's a unique closest point, it claims this tile
        if len(surrounds) == 1:
            new[x, y] = surrounds.pop()
        # If there's more than one closest point, this tile becomes no-man's land
        elif len(surrounds) > 1:
            new[x, y] = -1
    grid = new

# If you spend a while doing some taxicab geometry, you can prove that the
# infinite regions are exactly those that touch the boundary of the bounding
# rectangle:
boundary = np.concatenate((grid[0, :], grid[-1, :],
                           grid[:, 0], grid[:, -1]))
infinite = set(boundary)
vals, counts = np.unique(grid, return_counts=True)
count = max(c for v, c in zip(vals, counts)
            if v not in infinite)
print(count)
