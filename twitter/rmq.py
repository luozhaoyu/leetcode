#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    rmq.py
    ~~~~~~~~~~~~~~

    A brief description goes here.
"""
import re

def main(argv):
    N, M = re.split(r'\s+', raw_input())
    N = int(N)
    M = int(M)
    arrs = [int(i) for i in re.split(r'\s+', raw_input())]
    lrs = []
    for i in range(M):
        l, r = re.split(r'\s+', raw_input())
        l = int(l)
        r = int(r)
        lrs.append([l, r])
#    N = 10
#    M = 5
#    arrs = [10, 20, 30, 40, 11, 22, 33, 44, 15, 5]
#    lrs = [[0, 5], [1, 2], [8, 9], [0, 9], [4, 6]]

    for i in lrs:
        l, r = i
        tmp = arrs[l: r+1]
        if tmp:
            m = min(arrs[l: r+1])
            print m
        else:
            print


if __name__ == '__main__':
    import sys
    main(sys.argv)
