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
        self.started = False
        self.finished = False

    @property
    def cost(self):
        return 61 + ord(self.name.lower()) - ord('a')

    @staticmethod
    def get(name):
        if name not in steps:
            steps[name] = Step(name)
        return steps[name]

    def waiting(self):
        return not self.finished and not self.started

    def ready(self):
        return self.waiting() and all(step.finished for step in self.prereqs)

    def __repr__(self):
        return self.name

class Worker:
    def __init__(self):
        self.job = None
        self.progress = 0

    def work_on(self, job, callback):
        self.job = job
        self.progress = 0
        self._callback = callback
        job.started = True

    def tick(self):
        if self.busy():
            self.progress += 1
            if self.job.cost == self.progress:
                self.job.finished = True
                self._callback(self.job.name)
                self.job = None 

    def busy(self):
        return self.job is not None

    def status(self):
        return '.' if self.job is None else self.job.name

for line in sys.stdin.readlines():
    sfrom, sto = parse_edge(line)
    a, b = Step.get(sfrom), Step.get(sto)
    a.heirs += [b]
    b.prereqs += [a]

# This does a bunch of unnecessary scans, but the input is tiny so whatever.
sequence = ''
def add_to_sequence(s):
    global sequence
    sequence += s

workers = {Worker() for i in range(5)}
clock = 0
while any(s for s in steps.values() if not s.finished):
    available_workers = [w for w in workers if not w.busy()]
    ready_jobs = sorted((k, step)
                        for k, step in steps.items()
                        if step.ready())
    while available_workers and ready_jobs:
        worker = available_workers.pop(0)
        k, job = ready_jobs.pop(0)
        worker.work_on(job, add_to_sequence)
    for worker in workers:
        worker.tick()
    clock += 1
print(clock)
