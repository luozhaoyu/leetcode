class Solution:

    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        if s == p:
            return True
        if not p:
            return False
        tmp = p.replace('*', '')
        if len(tmp) > len(s):
            return False
        if not s:
            if not tmp:
                return True
            else:
                return False

        current_reachable = []
        if p[0] == '?' or p[0] == s[0]:
            current_reachable = [0]
        elif p[0] == '*':
            current_reachable = range(-1, len(s))
        else:
            return False

        for pi in p[1:]:
            if pi == '?':
                current_reachable = [i+1 for i in current_reachable if i+1 <= len(s) - 1]
                if not current_reachable:
                    return False
            elif pi == '*':
                current_reachable = range(min(current_reachable or [-1]), len(s))
            else:
                new_reachable = []
                for reachable in current_reachable:
                    if reachable + 1 <= len(s) - 1 and s[reachable+1] == pi:
                        new_reachable.append(reachable+1)
                current_reachable = new_reachable
                if not current_reachable:
                    return False

        if len(s) - 1 in current_reachable:
            return True
        else:
            return False


        
so = Solution()
ls = ["aa", "aa", "aaa", "aa", "aa", "ab", "aab", "axxbxxycxxde", "axxbc", "bac?d?", "b", "aaaaaaaaaaaaaaaaaaaaaaaaa", ""]
lp = ["a", "aa", "aa", "*", "a*", "?*", "c*a*b", "a**?*??b???c?d*?*e", "a*b*c", "*b?c?d?", "*?*?*", "*aaaaa*", "*"]
for s,p in zip(ls, lp):
    line = "%s, %s -> %s" % (s, p, so.isMatch(s, p))
    print line

s, p = [
#"a" * 32316, "*%s*" % ("a" * 32317)
]
line = "%s, %s -> %s" % (s, p, so.isMatch(s, p))
print line
