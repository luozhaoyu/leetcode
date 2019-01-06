#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Brief Summary
Attributes:

Google Python Style Guide:
    http://google-styleguide.googlecode.com/svn/trunk/pyguide.html
"""
import copy
__copyright__ = "Zhaoyu Luo"

import unittest
#import mock

def test_can_arrange():
    tests = ["aa", "abc", "", "aabb", "aba", "baa"]
    for s in tests:
        print s, can_arrange_palindrome2(s)

def test_rearrange():
    tests = ["aa", "abc", "", "aabb", "aba", "baa", "abcdabcd"]
    for s in tests:
        res = rearrange(s)
        print s, res, len(res)

def can_arrange_palindrome(s):
    if not s:
        return True

    def count(s):
        occurrences = {}
        # O(n)
        for c in s:
            if c in occurrences:
                occurrences[c] += 1
            else:
                occurrences[c] = 1
        return occurrences
    occurrences = count(s)


    number_of_odds = 0
    # O(1~n)
    for c in occurrences:
        if occurrences[c] % 2 != 0:
            number_of_odds += 1
            if number_of_odds > 1:
                return False
    return True

def can_arrange_palindrome2(s):
    if not s:
        return True

    occurrences = {}
    number_of_odds = 0
    # O(n)
    for c in s:
        if c in occurrences:
            occurrences[c] += 1
            if occurrences[c] % 2 == 0:
                number_of_odds -= 1
            else:
                number_of_odds += 1
        else: # initial
            occurrences[c] = 1
            number_of_odds += 1

    if number_of_odds > 1:
        return False
    else:
        return True

def rec_rearrange(prefix, m):
    if not m:
        return [prefix]

    res = []
    for k in m:
        new_m = copy.copy(m)
        new_prefix = prefix + k
        if m[k] == 1:
            del new_m[k]
        else:
            new_m[k] -= 1
        res.extend(rec_rearrange(new_prefix, new_m))
    return res


def rearrange(s):
    """
    Args:
        s

    Returns:
        []
    """
    if not can_arrange_palindrome2(s):
        return []

    m = {}
    for c in s:
        if c in m:
            m[c] += 1
        else:
            m[c] = 1

    middle = ""
    for k in m:
        if m[k] % 2 == 0:
            m[k] /= 2
        else:
            middle = k
    if middle:
        del m[middle]
    res = rec_rearrange("", m)
    palindromes = []
    for i in res:
        palindromes.append(i + middle + "".join(list(i)[::-1]))

    return palindromes




def main():
    """Main function only in command line"""
    from sys import argv
    test_rearrange()



if __name__ == '__main__':
    main()
