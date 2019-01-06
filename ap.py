#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    ap.py
    ~~~~~~~~~~~~~~

    A brief description goes here.
"""

import re

def main(argv):
    N = int(raw_input())
    ints = [long(i) for i in re.split(r'\s+', raw_input())]
    gap0 = ints[1] - ints[0]
    gap1 = ints[2] - ints[1]
    if gap1 > gap0:
        print ints[1] + gap0
        return
    if gap0 > gap1:
        print ints[0] + gap1
        return

    gap = gap0

    for i in range(1, len(ints)):
        if ints[i] - ints[i - 1] > gap:
            print ints[i - 1] + gap
            return


if __name__ == '__main__':
    import sys
    main(sys.argv)
