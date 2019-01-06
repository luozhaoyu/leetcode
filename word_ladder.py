import pdb
def gap(a, b):
    res = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            res += 1
    return res

def get_neighbours(w):
    res = set()
    for i in range(len(w)):
        for c in range(26):
            res.add(w[:i] + chr(c + ord('a'))+ w[i+1:])
    res.remove(w)
    return res


class Word(object):
    def __init__(self, value, name="", prev=""):
        self.value = value
        self.name = name
        self.prev = prev
        self.index = None

    def __str__(self):
        return "[%s]%s:%s" % (self.index, self.name, self.value)
        return "[%s](%s)%s:%s" % (self.index, self.prev, self.name, self.value)


def sort_path(unsettled_path, changed):
    i = changed
    while (i-1) / 2 >= 0 and unsettled_path[i].value < unsettled_path[(i-1)/2].value:
        #print "fuck", i, unsettled_path[i], unsettled_path[i/2]
        unsettled_path[i], unsettled_path[(i-1)/2] = unsettled_path[(i-1)/2], unsettled_path[i]
        unsettled_path[i].index, unsettled_path[(i-1)/2].index = unsettled_path[(i-1)/2].index, unsettled_path[i].index
        assert unsettled_path[i].value >= unsettled_path[(i-1)/2].value
        i = (i-1) / 2
    #print 'after', changed, [str(k) for k in unsettled_path[:8]]
    return unsettled_path

class Solution:
    # @param {string} beginWord
    # @param {strig} endWord
    # @param {set<string>} wordDict
    # @return {integer}
    def ladderLength(self, beginWord, endWord, wordDict):
        if gap(beginWord, endWord) == 1:
            if wordDict:
                return 2
            else:
                return 0

        graph = {}
        max_length = len(beginWord) + 100
        #t0 = time.time()
        wordDict.add(endWord)
        wordDict.add(beginWord)

        def create_graph_by_exhaustive():
            for w in wordDict:
                neighbors = get_neighbours(w)
                graph[w] = neighbors.intersection(wordDict)
            return graph

        def create_graph_by_compare():
            for i in range(len(beginWord)):
                word_compare = {}
                for w in wordDict:
                    abbr = w[:i] + w[i+1:]
                    if abbr not in word_compare:
                        word_compare[abbr] = set()
                    word_compare[abbr].add(w)
                for abbr in word_compare:
                    for w in word_compare[abbr]:
                        if w not in graph:
                            graph[w] = set()
                        graph[w] = graph[w].union(word_compare[abbr])
            return graph

        graph = create_graph_by_compare()
        paths = {}
        unsettled_path = []
        for w in graph:
            if beginWord in graph[w]:
                paths[w] = Word(1, w, beginWord)
            else:
                paths[w] = Word(max_length, w, "")
            unsettled_path.append(paths[w])
        #t1 = time.time()

        min_time = 0
        count = 0
        miss = 0
        fail = 0
        unsettled_path = sorted(unsettled_path, key=lambda x: x.value)
        # initial min heap
        for i, p in enumerate(unsettled_path):
            p.index = i
        while unsettled_path:
            #print unsettled_path[0], [str(kk) for kk in unsettled_path[:10]]
            detour_length, detour_point = unsettled_path[0].value, unsettled_path[0].name
            #print detour_point, detour_length, [str(kk) for kk in unsettled_path[:20]]
            #tmin = time.time()
            if len(unsettled_path) > 1:
                try:
                    assert unsettled_path[0].value <= unsettled_path[1].value
                    if len(unsettled_path) > 2:
                        assert unsettled_path[0].value <= unsettled_path[2].value
                except AssertionError as e:
                    print len(unsettled_path), [str(kk) for kk in unsettled_path[:10]]
                    pdb.set_trace()
                    raise
                unsettled_path[0] = unsettled_path[-1]
                unsettled_path[0].index = 0
                i = 0
                while True:
                    if 2*i + 2 < len(unsettled_path): # I still have child
                        if unsettled_path[2*i+1].value <= unsettled_path[2*i+2].value and unsettled_path[2*i+1].value < unsettled_path[i].value:
                            unsettled_path[i], unsettled_path[2*i+1] = unsettled_path[2*i+1], unsettled_path[i]
                            unsettled_path[i].index, unsettled_path[2*i+1].index = unsettled_path[2*i+1].index, unsettled_path[i].index
                            assert unsettled_path[i].value <= unsettled_path[2*i+1].value
                            i = 2*i+1
                        elif unsettled_path[2*i+2].value <= unsettled_path[2*i+1].value and unsettled_path[2*i+2].value < unsettled_path[i].value:
                            unsettled_path[i], unsettled_path[2*i+2] = unsettled_path[2*i+2], unsettled_path[i]
                            unsettled_path[i].index, unsettled_path[2*i+2].index = unsettled_path[2*i+2].index, unsettled_path[i].index
                            assert unsettled_path[i].value <= unsettled_path[2*i+2].value
                            i = 2*i+2
                        else:
                            break
                    elif 2*i + 1 < len(unsettled_path) and unsettled_path[2*i+1].value < unsettled_path[i]:
                        unsettled_path[i], unsettled_path[2*i+1] = unsettled_path[2*i+1], unsettled_path[i]
                        unsettled_path[i].index, unsettled_path[2*i+1].index = unsettled_path[2*i+1].index, unsettled_path[i].index
                        assert unsettled_path[i].value <= unsettled_path[2*i+1].value
                        i = 2*i+1
                    else:
                        break
               # try:
               #     assert unsettled_path[0].value <= unsettled_path[1].value
               #     if len(unsettled_path) > 2:
               #         assert unsettled_path[0].value <= unsettled_path[2].value
               # except AssertionError as e:
               #     print i, len(unsettled_path), [str(kk) for kk in unsettled_path[:10]]
               #     pdb.set_trace()
               #     raise
            # no leaf now, means the last one
            unsettled_path.pop()

            if detour_length >= max_length: # minimum middle point is unreachable
                break
            else:
                for w in graph[detour_point]:
                    if w == beginWord or w == detour_point:
                        continue
                    count += 1
                    if 1 + detour_length < paths[w].value:
                       # assert unsettled_path[paths[w].index / 2].value <= paths[w].value
                       # if paths[w].index * 2 + 1 < len(unsettled_path):
                       #     assert paths[w].value <= unsettled_path[paths[w].index * 2 + 1].value
                       # if paths[w].index * 2 + 2 < len(unsettled_path):
                       #     assert paths[w].value <= unsettled_path[paths[w].index * 2 + 2].value
                        paths[w].value = 1 + detour_length
                        paths[w].prev = detour_point
                        unsettled_path = sort_path(unsettled_path, paths[w].index)
                    else:
                        fail += 1
            #print detour_point, detour_length, [str(kk) for kk in unsettled_path[:20]]

        def debug_path(paths):
            total = 0
            for k in paths:
                if paths[k].value < max_length:
                    total += 1
                print k, paths[k]
            return total
        #print paths[endWord], graph[endWord]
        #print len(unsettled_path), t1-t0, t2 -t1, min_time, count, miss, fail
        if paths[endWord].value >= max_length:
            return 0
        else:
            return paths[endWord].value + 1




so = Solution()
ls, le, ld = eval(open("input","r").read())
l = [
    ["hit", "cog", ["hot", "hit", "cog", "dot", "dog"]],
    [ls, le, ld],
    ["a", "c", ["a", "b", "c"]],
    ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]],
    ["hit", "cog", ["aaa"]],
    ["hit", "cog", []],
    ["a", "c", ["a", "b", "c"]],
    ["hot", "dog", ["hot", "dog"]],
]
for s, e, d in l:
    print s, e, len(d), so.ladderLength(s, e, set(d))
