#!/usr/bin/python3
import sys
import re

def parse_edge(line):
    m = re.match(r'Step (\w+) must be finished before step (\w+) can begin.', line)
    if not m:
        raise ValueError('Malformed input line.')
    return tuple(m.groups())

steps = dict()
class Step:
    def __init__(self, name):
        self.name = name
        self.prereqs = []
        self.heirs = []
        self.finished = False

    @staticmethod
    def get(name):
        if name not in steps:
            steps[name] = Step(name)
        return steps[name]

    def waiting(self):
        return not self.finished

    def ready(self):
        return not self.finished and not any(map(Step.waiting, self.prereqs))

for line in sys.stdin.readlines():
    sfrom, sto = parse_edge(line)
    a, b = Step.get(sfrom), Step.get(sto)
    a.heirs += [b]
    b.prereqs += [a]

# This does a bunch of unnecessary scans, but the input is tiny so whatever.
sequence = ''
while any(map(Step.waiting, steps.values())):
    letter, next_step = min((k, step)
                            for k, step in steps.items()
                            if step.ready())
    sequence += letter
    next_step.finished = True

print(sequence)
