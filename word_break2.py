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
        def dp():
            f = []
            for i in range(len(s)):
                f.append([])
                for j in range(i+1):
                    current_str = s[j: i+1]
                    if self.find_trie(current_str):
                        if f[j-1]:
                            f[i].append(j-1)
                        else:
                            if j == 0:
                                f[i].append(-1)
            if not f[-1]:
                return []
            print f

            opened = [[f[-1][0], len(s) - 1]]
            last_child = None
            generate_child = False
            # use backtracking too
            while opened:
                try:
                    prev, current = opened[0]
                    # then test new current
                    if prev == -1:
                        tmp = []
                        #opened[0][0] = 0
                        for i in range(0, len(opened)-1):
                            tmp.append(s[opened[i][0]+1: opened[i+1][0]+1])
                        tmp.append(s[opened[-1][0] + 1:])
                        result.append(tmp)
                        opened.pop(0)
                        last_child = current
                        generate_child = True
                        print opened, last_child
                    else: # insert previous
                        if generate_child:
                            print 'fuck', last_child
                            last_child_index = f[current].index(last_child)
                            if last_child_index + 1 == len(f[current]): # next exceed
                                last_child = current
                            else: # pick next child
                                opened.pop(0)
                                opened.insert(0,
                                    [f[current][last_child_index + 1], current])
                                last_child = None
                            generate_child = False
                            continue

                        generate_child = False
                        if not last_child:
                            opened.insert(0,
                                [f[prev][0], prev])
                            continue

                        opened.pop(0)
                        last_child_index = f[current].index(last_child)
                        print opened, f[current], last_child
                        if last_child_index + 1 == len(f[current]): # next exceed
                            last_child = current
                        else: # pick next child
                            opened.insert(0,
                                [f[current][last_child_index + 1], current])
                            last_child = None

                except:
                    print "ERROR", opened, current
                    print last_child
                    raise
            return result

        return dp()

so = Solution()
s, dicts = "catsanddog", ["cat", "cats", "and", "sand", "dog", "a", "nd", "ca", "ts"]
#s, dicts = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
import pprint
pprint.pprint(so.wordBreak(s, dicts))
for i in dicts:
    pprint.pprint(so.find_trie(i))

