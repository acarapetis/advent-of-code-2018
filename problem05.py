#!/usr/bin/python3

import sys
import re
import numpy as np

class Claim:
    CLAIM_LINE = re.compile(r'#(\d+)\s+(\d+),(\d+):\s+(\d+)x(\d+)')

    @staticmethod
    def parse(string):
        m = Claim.CLAIM_LINE.match(string)
        if not m:
            raise ValueError(f"Invalid claim input {string}")
        _, x, y, xw, yw = m.groups()
        return Claim(x, y, xw, yw)

    def __init__(self, x, y, xw, yw):
        self.x = x
        self.y = y
        self.xw = xw
        self.yw = yw

    @property
    def xmax(self):
        return self.x + self.xw

    @property
    def ymax(self):
        return self.y + self.yw

    def painton(self, canvas: np.ndarray):
        canvas[self.x:self.xmax, self.y:self.ymax] += 1

claims = list(map(Claim.parse, sys.stdin.readlines()))
xmax = max(claims, key=lambda c: c.xmax)
ymax = max(claims, key=lambda c: c.ymax)
canvas = np.zeros((xmax, ymax), dtype=int)
for c in claims:
    c.painton(canvas)

print(np.sum(canvas >= 2))
