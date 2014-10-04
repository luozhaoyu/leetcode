# -*- coding: utf-8 -*-
"""
    word_ladder_2.py
    ~~~~~~~~~~~~~~

    A brief description goes here.
"""
import copy
import time
class Solution:

    # @param start, a string

    # @param end, a string

    # @param dictionary, a set of string

    # @return a list of lists of string
    MAX_EDGE_VALUE = 9999

    def findLadders(self, start, end, dictionary):
        Solution.access_cache = {}
        return self.shortest_path(start, end, dictionary)

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

    def get_edges(self, start, end, dictionary):
        edges = {}
        d = set(copy.copy(dictionary))
        d.add(start)
        d.add(end)
        for i in d:
            for j in self.get_possible_changes(i, d):
                if edges.has_key(i):
                    edges[i][j] = 1
                else:
                    edges[i] = {j: 1}
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
            #whole_paths = [[end, i] for i in paths[end]['previous']]
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

        t1 = time.time()
        edges = self.get_edges(start, end, dictionary)
        if not start in edges:
            return []
        t11 = time.time()

        shortest_paths = {}
        for i in edges[start]:
            shortest_paths[i] = {
                'value': edges[start][i]
            }
        unresolved_verticles = set(dictionary)
        unresolved_verticles.add(end)

        t2 = time.time()

        while unresolved_verticles:
            current_min_verticle = get_min_edge(unresolved_verticles, shortest_paths)
            if current_min_verticle == end: # if the end is specified, bread directly
                break

            for destination in self.get_possible_changes(current_min_verticle, dictionary):
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
            unresolved_verticles.remove(current_min_verticle)
        t3 = time.time()
        paths = get_all_paths(end, shortest_paths)
        t4 = time.time()
        print "%.4f\t%.4f\t%.4f" % (t11 - t1, t2 - t11, t4 - t3)
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
        return False

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
    start, end, d = "a", "c", ["a","b","c"]
    start, end, d = "hot", "dog", ["hot","dog"]
    start, end, d = "hit", "cog", ["hot","cog","dot","dog","hit", "lot", "log"]
    start, end, d = "magic", "pearl", ["flail","halon","lexus","joint","pears","slabs","lorie","lapse","wroth","yalow","swear","cavil","piety","yogis","dhaka","laxer","tatum","provo","truss","tends","deana","dried","hutch","basho","flyby","miler","fries","floes","lingo","wider","scary","marks","perry","igloo","melts","lanny","satan","foamy","perks","denim","plugs","cloak","cyril","women","issue","rocky","marry","trash","merry","topic","hicks","dicky","prado","casio","lapel","diane","serer","paige","parry","elope","balds","dated","copra","earth","marty","slake","balms","daryl","loves","civet","sweat","daley","touch","maria","dacca","muggy","chore","felix","ogled","acids","terse","cults","darla","snubs","boats","recta","cohan","purse","joist","grosz","sheri","steam","manic","luisa","gluts","spits","boxer","abner","cooke","scowl","kenya","hasps","roger","edwin","black","terns","folks","demur","dingo","party","brian","numbs","forgo","gunny","waled","bucks","titan","ruffs","pizza","ravel","poole","suits","stoic","segre","white","lemur","belts","scums","parks","gusts","ozark","umped","heard","lorna","emile","orbit","onset","cruet","amiss","fumed","gelds","italy","rakes","loxed","kilts","mania","tombs","gaped","merge","molar","smith","tangs","misty","wefts","yawns","smile","scuff","width","paris","coded","sodom","shits","benny","pudgy","mayer","peary","curve","tulsa","ramos","thick","dogie","gourd","strop","ahmad","clove","tract","calyx","maris","wants","lipid","pearl","maybe","banjo","south","blend","diana","lanai","waged","shari","magic","duchy","decca","wried","maine","nutty","turns","satyr","holds","finks","twits","peaks","teems","peace","melon","czars","robby","tabby","shove","minty","marta","dregs","lacks","casts","aruba","stall","nurse","jewry","knuth"]


    begin = time.time()
    print start, end, len(d)
    print s.findLadders(start, end, d)
    end = time.time()
    print end - begin

if __name__ == '__main__':
    import sys
    _main(sys.argv)
