class Solution:

    # @param s, an input string

    # @param p, a pattern string

    # @return a boolean
    def shrink(self, pattern):
        shrinked = []
        i = 0
        while i < len(pattern):
            stars = 0
            questions = 0
            while i < len(pattern) and pattern[i] in ['*', '?']:
                if pattern[i] == '*':
                    stars += 1
                else:
                    questions += 1
                i += 1
            if stars == 0:
                if questions > 0:
                    shrinked.extend(['?'] * questions)
            else:
                shrinked.append(('*', questions))

            if i < len(pattern):
                shrinked.append(pattern[i])
            i += 1
        return shrinked

    def compress_string_score(self, string_score, pattern_list):
        compressed = []
        i = 0
        while i < len(string_score):
            p = pattern_list[string_score[i]]
            compressed.append(p)
            repeat = 0
            while p != '?' and i < len(string_score)-1 and\
                string_score[i + 1] == string_score[i]:
                repeat += 1
                i += 1
            if repeat:
                compressed.append(('*', repeat))
            i += 1
        return compressed

    def isMatch(self, s, p):

        pl = self.shrink(p)
        string_score = []
        cursor = 0
        for c in s:
            try:
                while cursor < len(pl) and isinstance(pl[cursor], tuple):
                    cursor += 1
                if cursor >= len(pl):
                    # pattern exhausted, while string exists
                    break

                # cursor is not a star
                if c == pl[cursor] or pl[cursor] == '?':
                    string_score.append(cursor)
                    # move on until meets with an alphabetic
                    cursor += 1
                else:
                    if string_score:
                        string_score.append(string_score[-1])
                    else:
                        return False
            except:
                print "%s: %s vs %s: %s" % (s, c, pl, cursor)
                print string_score
                raise
        compressed = self.compress_string_score(string_score, pl)
        print "%s %s vs %s" % (string_score, compressed, pl)
        for c_single, p_single in zip(compressed, pl):
            if c_single != p_single:
                if isinstance(c_single, tuple) and isinstance(p_single, tuple)\
                    and c_single[1] > p_single[1]:
                        continue
                else:
                    return False
        return True

so = Solution()
ls = ["aa", "aa", "aaa", "aa", "aa", "ab", "aab", "axxbxxycxxde"]
lp = ["a", "aa", "aa", "*", "a*", "?*", "c*a*b", "a**?*??b???c?d*?*e"]
for s,p in zip(ls, lp):
    line = "%s, %s -> %s" % (s, p, so.isMatch(s, p))
    print line
