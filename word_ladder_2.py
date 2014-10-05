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
    MAX_EDGE_VALUE = 9999

    def findLadders(self, start, end, dictionary):
        Solution.access_cache = {}
        return self.shortest_path(start, end, dictionary)
        #return self.breath_first_search(start, end, dictionary)

    def can_access(self, a, b):
        diff = 0
        i = 0
        try:
            while i < len(a):
                if a[i] != b[i]:
                    diff += 1
                    if diff >= 2:
                        return False
                i += 1
        except:
            raise
        return True

    def iterate_character(self, current, dict_set, visited_set):
        s1 = set()
        for i in range(len(current)):
            for j in range(1, 26):
                new_word = current[0:i] +\
                    chr((ord(current[i]) - ord('a') + j) % 26 + ord('a')) + current[i+1:]
                s1.add(new_word)
        s = s1.intersection(dict_set) - visited_set
        return s

    def get_possible_changes(self, current, dictionary):
        if Solution.access_cache.has_key(current):
            return Solution.access_cache[current]

        def iterate_all_possibility():
            s = set()
            for i in dictionary:
                if current != i and self.can_access(current, i):
                    s.add(i)
            return s

        #s = iterate_character()
        s = iterate_all_possibility()
        Solution.access_cache[current] = copy.copy(s)
        return s

    def get_edges(self, start, end, dictionary):

        d = set(copy.copy(dictionary))
        d.add(start)
        d.add(end)
        edges = {}
        for i in d: # optimization, uniformed initialization
            edges[i] = {}

        dict_set = set(dictionary)
        visited_set = set()
        for i in d:
            iterable_words = self.iterate_character(i, dict_set, visited_set)
            for j in iterable_words:
                edges[i][j] = 1
                edges[j][i] = 1
            visited_set.add(i)
        return edges

    def shortest_path(self, start, end, dictionary):
        def get_min_edge(verticles, shortest_paths):
            min_value = Solution.MAX_EDGE_VALUE
            min_verticle = None
            for i in verticles:
                if shortest_paths.has_key(i) and shortest_paths[i]['value'] < min_value:
                    min_value = shortest_paths[i]['value']
                    min_verticle = i
            return min_verticle

        def get_all_paths(end, paths):
            whole_paths = [[end]]
            result = []
            while whole_paths:
                path = whole_paths.pop()
                proceed = path[-1]
                if shortest_paths[proceed].has_key('previous'):
                    for i in shortest_paths[proceed]['previous']:
                        l = copy.copy(path)
                        l.append(i)
                        whole_paths.append(l)
                else:
                    path.append(start)
                    path.reverse()
                    result.append(path)
            return result

        edges = self.get_edges(start, end, dictionary)
        if not start in edges:
            return []

        shortest_paths = {}
        for i in edges[start]:
            shortest_paths[i] = {
                'value': edges[start][i]
            }
        unresolved_verticles = set(dictionary)
        unresolved_verticles.add(end)

        while unresolved_verticles:
            current_min_verticle = get_min_edge(unresolved_verticles, shortest_paths)
            if current_min_verticle == end: # if the end is specified, bread directly
                break
            elif current_min_verticle == None:
                print shortest_paths, unresolved_verticles
                print Solution.access_cache
                return []

            unresolved_verticles.remove(current_min_verticle)
            for destination in edges[current_min_verticle]:
                new_path_value = shortest_paths[current_min_verticle]['value'] + edges[current_min_verticle][destination]
                if not shortest_paths.has_key(destination):
                    shortest_paths[destination] = {
                        'value': new_path_value,
                        'previous': [current_min_verticle],
                    }
                else:
                    if new_path_value < shortest_paths[destination]['value']:
                        shortest_paths[destination] = {
                            'value': new_path_value,
                            'previous': [current_min_verticle],
                        }
                    elif new_path_value == shortest_paths[destination]['value']:
                        shortest_paths[destination]['previous'].append(current_min_verticle)
        paths = get_all_paths(end, shortest_paths)
        return paths

    def breath_first_search(self, start, end, dictionary):
        max_path_len = len(dictionary)
        i = 1
        while i<=max_path_len:
            print 'trying %i...' % i
            paths = self.depth_first_search(i, start, end, dictionary)
            if paths:
                return paths
            else:
                i += 1
        return []

    def get_current_possible_changes(self, current, dictionary, tried):
        s = self.get_possible_changes(current, dictionary)
        result = s - set(tried)
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
    datas = [["hit", "cog", ["hot","dot","dog","lot","log"]],
        ["a", "c", ["a","b","c"]],
        ["hot", "dog", ["hot","dog"]],
        ["hit", "cog", ["hot","cog","dot","dog","hit", "lot", "log"]],
        ]

    for start, end, d in datas:
        begin = time.time()
        print start, end, len(d)
        print s.findLadders(start, end, d)
        end = time.time()
        print end - begin

if __name__ == '__main__':
    import sys
    _main(sys.argv)
