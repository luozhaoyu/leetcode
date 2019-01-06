#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    prime.py
    ~~~~~~~~~~~~~~

    A brief description goes here.
"""
import math
def getNumberOfPrimes(n):
    n = int(n)
    if n <= 2:
        return 0
    elif n == 3:
        return 2

    primes = [2]
    for i in range(3, n):
        for j in primes:
            if j > int(math.sqrt(i)): # new prime
                primes.append(i)
                break
            else:
                if i % j == 0:
                    break
    return primes[-1]

def main(argv):
    _a = input();
    res = getNumberOfPrimes(_a);
    print res;



if __name__ == '__main__':
    import sys
    main(sys.argv)
