#!/usr/bin/python3
import sys
import numpy as np
from scipy.spatial.distance import cdist

coords = [tuple(int(s.strip()) for s in l.strip().split(','))
          for l in sys.stdin.readlines()]
xmax = max(x for x, y in coords)
ymax = max(y for x, y in coords)
shape = (xmax + 1, ymax + 1)
R = max(*shape)

grid = np.zeros(shape, dtype=int)
# this can't be the easiest way to do this...
indices = np.asarray(list(np.ndindex(grid.shape)))
dist = cdist(indices, coords, metric='cityblock')
cost = np.sum(dist, axis=1)

print(np.count_nonzero(cost < 10000))
