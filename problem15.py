#!/usr/bin/python3
import sys
from collections import namedtuple
class Node(namedtuple('Node', ['children', 'metadata'])):
    def walk(self):
        yield self
        for n in self.children:
            for w in n.walk():
                yield w

def parse_node(data):
    """Given a data string containing a node and possibly some more trailing
    data, return a tuple containing the Node and the remainder."""
    child_count = data.pop(0)
    meta_count = data.pop(0)
    children = []
    for i in range(child_count):
        child, data = parse_node(data)
        children.append(child)
    metadata = data[:meta_count]
    remainder = data[meta_count:]
    return Node(children, metadata), remainder

data = list(map(int, sys.stdin.read().split()))
tree, junk = parse_node(data)
if junk:
    raise ValueError("Leftover data after parsing tree!?")

if __name__ == '__main__':
    answer = sum(sum(node.metadata)
                 for node in tree.walk())

    print(answer)
