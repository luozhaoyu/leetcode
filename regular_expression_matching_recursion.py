class Solution(object):
    """Google interview"""
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == p:
            return True
        if not p:
            return not s
        if not s:
            return len(p) >= 2 and p[1] == "*" and self.isMatch(s, p[2:])
        if p == ".*":
            return True
        if p == ".":
            return len(s) == 1
        if len(p) == 1:
            return s == p

        # print(s, p)

        first_match = p[0] == s[0]

        if p[1] == "*":  # match empty or 1
            if p[0] == ".":
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        if p[0] == ".":
            return self.isMatch(s[1:], p[1:])
        return first_match and self.isMatch(s[1:], p[1:])


solution = Solution()
print(solution.isMatch("aa", "a"))
print(solution.isMatch("aa", "a*"))
print(solution.isMatch("ab", ".*"))
print(solution.isMatch("aab", "c*a*b"))
print(solution.isMatch("mississippi", "mis*is*p*."))
print(solution.isMatch("mississippi", "mis*is*ip*."))
print(solution.isMatch("a", "ab*a"))
print(solution.isMatch("mississippi", "mis*is*p*."))
print(solution.isMatch("bbbba", ".*a*a"))
print(solution.isMatch("ab", ".*.."))
print(solution.isMatch("bbaa", "a..."))
print(solution.isMatch("", "c*c*"))
