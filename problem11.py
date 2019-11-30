#!/usr/bin/python3
import sys
import numpy as np
from scipy.spatial.distance import cdist

sources = [tuple(int(s.strip()) for s in l.strip().split(','))
          for l in sys.stdin.readlines()]
xmax = max(x for x, y in sources)
ymax = max(y for x, y in sources)
shape = (xmax + 1, ymax + 1)

# list of coordinates of grid tiles
indices = np.asarray(list(np.ndindex(shape)))
# dist[i,j] is distance from source i to tile j:
dist = cdist(sources, indices, metric='cityblock')
# mindist[j] is distance of closest source to tile j:
mindist = np.min(dist, axis=0)
# unique_minimizers[j] is number of sources achieving mindist to tile j:
unique_minimizers = np.count_nonzero(dist == mindist, axis=0) == 1

outvals = ((unique_minimizers-1) # -1 where minimizer is not unique
           + unique_minimizers*(np.argmin(dist, axis=0)+1)) # index of minimizing source
grid = np.reshape(outvals, shape)

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
