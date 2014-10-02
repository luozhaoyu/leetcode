# -*- coding: utf-8 -*-
"""
    word_ladder_2.py
    ~~~~~~~~~~~~~~

    A brief description goes here.
"""
class Solution:

    # @param start, a string

    # @param end, a string

    # @param dict, a set of string

    # @return a list of lists of string

    def findLadders(self, start, end, dict):
        # BFS
        max_path_len = len(dict)
        i = 1
        while i<=max_path_len:
            paths = self.depth_first_search(i, start, end, dict)
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

    def get_all_accessible_change(self, current, dict):
        l = []
        for i in dict:
            if self.can_access(current, i) and current != i:
                l.append(i)
        return l

    def depth_first_search(self, max_depth, start, end, dict):
        stack = [start]
        result = []
        state = []
        tried = set()
        depth = 0

        while stack:
            try:
                current = stack.pop()
                tried.add(current)
                state.append(current)
                depth += 1
                if depth == max_depth: # final chance
                    if current == end:
                        print state
                        result.add(state)
                    else: # backtracking
                        while state:
                            last = state[-1]
                            if last in tried: # until meet a node, which has not been tried
                                state.pop()
                                depth -= 1
                            else: # 
                                continue
                else:
                    available_nodes = get_all_accessible_change(current, dict)
                    for i in available_nodes:
                        if not i in tried:
                            stack.append(i)
            except:
                print "depth=%i, state=%s\ntried=%s\nresult=%s" % (depth, state, tried, result)
                raise
        return result

def _main(argv):
    s = Solution()
    start = "hit"
    end = "cog"
    d = ["hot","dot","dog","lot","log"]
    s.findLadders(start, end, d)

if __name__ == '__main__':
    import sys
    _main(sys.argv)
