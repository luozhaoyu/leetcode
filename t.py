#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    t.py
    ~~~~~~~~~~~~~~

    A brief description goes here.
"""


def main(argv):
    n = int(raw_input())
    indexes = []
    for i in range(n):
        index = int(raw_input())
        indexes.append(index)
    tree = [1]
    max_cycle = max(indexes)
    for i in range(1, max_cycle+1):
        if i % 2 == 0:
            tree.append(tree[i-1] + 1)
        else:
            tree.append(tree[i-1] * 2)
    for i in indexes:
        print tree[i]


if __name__ == '__main__':
    import sys
    main(sys.argv)
