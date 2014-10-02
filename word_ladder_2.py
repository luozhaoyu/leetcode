# -*- coding: utf-8 -*-
"""
    word_ladder_2.py
    ~~~~~~~~~~~~~~

    A brief description goes here.
"""
import copy
class Solution:

    # @param start, a string

    # @param end, a string

    # @param dictionary, a set of string

    # @return a list of lists of string
    access_cache = {}

    def findLadders(self, start, end, dictionary):
        # BFS
        max_path_len = len(dictionary)
        i = 1
        while i<=max_path_len:
            print 'trying %i...' % i
            paths = self.depth_first_search(i, start, end, dictionary)
            if paths:
                return paths
            else:
                i += 1
        return False

    def can_access(self, a, b):
        for i in range(0, len(a)):
            a_ = [j for j in a]
            b_ = [j for j in b]
            a_[i] = ''
            b_[i] = ''
            if a_ == b_:
                return True
        return False

    def get_possible_changes(self, current, dictionary):
        if Solution.access_cache.has_key(current):
            return Solution.access_cache[current]

        s = set()
        for i in dictionary:
            if self.can_access(current, i) and current != i:
                s.add(i)
        Solution.access_cache[current] = copy.copy(s)
        return s

    def get_current_possible_changes(self, current, dictionary, tried):
        result = set()
        s = self.get_possible_changes(current, dictionary)
        for i in s:
            if not i in tried:
                result.add(i)
        return result

    def depth_first_search(self, max_depth, start, end, dictionary):
        stack = [start]
        result = []
        state = []
        tried = set()

        while stack:
            try:
                current = stack[-1]
                state.append(current)
                if len(state) == max_depth: # final chance
                    if self.can_access(current, end):
                        result.append(copy.copy(state))

                    while stack and state and stack[-1] == state[-1]:
                        stack.pop()
                        state.pop()
                else:
                    available_nodes = self.get_current_possible_changes(current, dictionary, state)
                    if available_nodes:
                        for i in available_nodes:
                            stack.append(i)
                    else: # backtracking
                        while stack and state and stack[-1] == state[-1]:
                            stack.pop()
                            state.pop()
            except:
                print "state=%s\ntried=%s\nresult=%s" % (state, tried, result)
                raise
        return result

def _main(argv):
    import time
    s = Solution()
    start, end, d = "hit", "cog", ["hot","dot","dog","lot","log"]

    begin = time.time()
    print start, end, len(d)
    print s.findLadders(start, end, d)
    end = time.time()
    print end - begin

if __name__ == '__main__':
    import sys
    _main(sys.argv)
