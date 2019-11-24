#!/usr/bin/python3

import re
import sys
from collections import defaultdict
import numpy as np

lines = sorted(sys.stdin.readlines())

guards = defaultdict(lambda: np.zeros(60, dtype=int))

LOG_LINE = re.compile(r'\[\d+-\d+-\d+\s+\d+:(\d+)\]\s+(.*)')
NEW_GUARD = re.compile(r'Guard #(\d+) begins shift')

asleep = False
bedtime = 0
guard = None
for l in lines:
    m = LOG_LINE.match(l)
    if not m:
        raise ValueError
    minute, msg = m.groups()
    minute = int(minute)

    m = NEW_GUARD.match(msg)
    if m:
        if asleep:
            guard[bedtime:60] += 1
        guard = guards[m.group(1)]
        asleep = False

    elif 'falls asleep' in msg:
        if asleep:
            raise ValueError("Can't fall asleep if already asleep!")
        asleep = True
        bedtime = minute

    elif 'wakes up' in msg:
        if not asleep:
            raise ValueError("Can't wake up if not asleep!")
        asleep = False
        guard[bedtime:minute] += 1

id, mins = max(guards.items(), key=lambda pair: np.max(pair[1]))
print(int(id)*np.argmax(mins))

