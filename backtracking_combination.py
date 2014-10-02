#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    backtracking_combination.py
    ~~~~~~~~~~~~~~

    A brief description goes here.
"""
import copy

def bt_r(depth, n, k, stack):
    if depth == k:
        print stack
        return stack
    else: # depth < k
        if stack:
            last = stack[-1]
        else:
            last = 0
        for i in range(last+1, n+1):
            new_stack = copy.copy(stack)
            new_stack.append(i)
            bt_r(depth+1, n, k, new_stack)


def bt(n, k):
    stack = [1]
    while stack:
        current = stack[-1]
        if len(stack) == k: # fit
            if current <= n:
                print stack
                current += 1
                stack[-1] = current
            else:
                stack.pop()
                stack[-1] += 1
        else:
            if current > (n - k + len(stack)):
                stack.pop()
                if stack:
                    stack[-1] += 1
            else:
                stack.append(current + 1)


def main(argv):
    #bt_r(0, 10, 5, [])
    bt(10, 5)


if __name__ == '__main__':
    import sys
    main(sys.argv)
