#!/usr/bin/python3
from problem15 import tree

# This one is pretty easy - just write out value as a recursive function.
# Pretty much a direct translation of the definition in the problem.
def value(node):
    if not node.children:
        return sum(node.metadata)
    return sum(value(node.children[m-1])
               for m in node.metadata
               if m > 0 and m - 1 < len(node.children))

if __name__ == '__main__':
    print(value(tree))
