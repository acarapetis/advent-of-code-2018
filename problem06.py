#!/usr/bin/python3

import sys
import re
import numpy as np

class Claim:
    CLAIM_LINE = re.compile(r'#(\d+)\s+@\s+(\d+),(\d+):\s+(\d+)x(\d+)')

    @staticmethod
    def parse(string):
        m = Claim.CLAIM_LINE.match(string)
        if not m:
            raise ValueError(f"Invalid claim input {string}")
        id, x, y, xw, yw = m.groups()
        return Claim(id, x, y, xw, yw)

    def __init__(self, id, x, y, xw, yw):
        self.id = int(id)
        self.x = int(x)
        self.y = int(y)
        self.xw = int(xw)
        self.yw = int(yw)

    @property
    def xmax(self):
        return self.x + self.xw

    @property
    def ymax(self):
        return self.y + self.yw

    def sliceof(self, canvas: np.ndarray):
        return canvas[self.x:self.xmax, self.y:self.ymax]

    def painton(self, canvas: np.ndarray):
        canvas[self.x:self.xmax, self.y:self.ymax] += 1

    def __str__(self):
        return "#{id} @ {x},{y}: {xw}x{yw}".format(**vars(self))

claims = list(map(Claim.parse, sys.stdin.readlines()))
xmax = max(c.xmax for c in claims)
ymax = max(c.ymax for c in claims)
canvas = np.zeros((xmax, ymax), dtype=int)
for c in claims:
    c.painton(canvas)

for c in claims:
    if np.all(c.sliceof(canvas) == 1):
        print(c)
