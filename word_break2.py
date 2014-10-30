import copy
class Solution:
    def find_trie(self, word):
        """
        Returns:
            True: find
            None: not complete match
            False: not match
        """
        if not word:
            return False

        current_root = self.trie
        for c in word:
            if c in current_root['next'].keys(): # match
                current_root = current_root['next'][c]
            else:
                return False
        if current_root['value'] == c:
            return True
        elif current_root['value'] == None:
            return None
        else:
            return False

    def insert_trie(self, word, root):
        """
        Args:
            root: {'value': c, 'next': {'a': root, 'b': root}}
        """
        current_root = root
        i = 0
        while i < len(word):
            c = word[i]
            #if c in [current_root['next'][k]['value'] for k in current_root['next']]: # match
            if c in current_root['next'].keys(): # match
                current_root = current_root['next'][c]
            else: # does not match, break to create new
                break
            i += 1

        while i < len(word):
            c = word[i]
            new_node = {
                'value': None,
                'next': {},
            }
            current_root['next'][c] = new_node
            current_root = new_node
            i += 1
        current_root['value'] = c
        return current_root

    def create_trie(self, dicts):
        self.trie = {'value': None, 'next': {}}
        for w in dicts:
            self.insert_trie(w, self.trie)
        return self.trie

    # @param s, a string

    # @param dict, a set of string

    # @return a list of strings

    def wordBreak(self, s, dicts):
        self.trie = self.create_trie(dicts)
        result = []
#        print self.trie
#        for i in ['c', 'cat', 'ca']:
#            print self.find_trie(i)
        import pprint
        pprint.pprint(self.trie)
        def dp():
            f = []
            for i in range(len(s)):
                f.append([])
                for j in range(i+1):
                    current_str = s[j: i+1]
                    if self.find_trie(current_str):
                        print s[:i+1], current_str, i, j
                        if f[j-1]:
                            print 'ha'
                            f[i].append(j-1)
                        else:
                            if j == 0:
                                f[i].append(-1)
            print f
            opened = copy.copy(f[-1])
            last = len(s) - 1
            current = None
            # use backtracking too
            while opened:
                try:
                    if not current: # will only use for once
                        current = opened[0]
                        last = opened[0]
                    else:
                        current_index = f[last].index(current)
                        if current_index + 1 == len(f[last]): # next exceed
                            opened.pop(0)
                            current = opened[0]
                        else:
                            current = f[last][current_index + 1] # pick next

                    print opened, current, last, s[current+1: last+1]
                    # then test new current
                    if current == -1:
                        tmp = []
                        for i in range(0, len(opened)-1):
                            tmp.append(s[opened[i]: opened[i+1]+1])
                        result.append(tmp)
                        opened.pop(0)
                        current = None
                    else: # insert previous
                        opened.insert(0, f[current][0])
                        last = current
                        current = opened[0]
                except:
                    print "ERROR"
                    print opened, current, last
                    raise
            return result

        def backtrace():
            i = 0
            opened = [[i, -1]] # it will move ahead then
            while opened:
                # move ahead
                opened[-1][1] += 1
                current_str = s[opened[-1][0]: opened[-1][1] + 1]
                if opened[-1][1] == len(s) - 1:
                    print opened, current_str
                    if self.find_trie(current_str): # match fully
                        bingo = []
                        for i in opened:
                            bingo.append(s[i[0]:i[1]+1])
                        result.append(bingo)
                    else:
                        opened.pop()
                elif opened[-1][1] >= len(s):
                    opened.pop()
                else:
                    match = self.find_trie(current_str)
                    if match: # match completely, then add it
                        opened.append([opened[-1][1] + 1, opened[-1][1]])
                    elif match == None: # match partially
                        continue
                    else:
                        opened.pop()
            return result
        return dp()

so = Solution()
s, dicts = "catsanddog", ["cat", "cats", "and", "sand", "dog", "a", "nd"]
#s, dicts = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
import pprint
pprint.pprint(so.wordBreak(s, dicts))
for i in dicts:
    pprint.pprint(so.find_trie(i))

