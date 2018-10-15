class Solution(object):
    """Google interview"""
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        results = {}
        def dp(i, j):
            return results.get((i, j), False)

        # -1 means empty
        results[-1, -1] = True
        # "" matches ".*" "\w*" needs special care
        i = 1
        while i < len(p):
            if p[i] == "*":
                results[-1, i] = True
            else:
                break
            i += 2

        for i in range(len(s)):
            for j in range(len(p)):
                one_match = s[i] == p[j-1] or p[j-1] == "."
                if p[j] == "*":
                    # * either match empty or match \w+, which means p[j-1:j] will resolve to at least 1 character, which means p[:j] will still match s[:i-1]
                    match = dp(i, j-2) or (one_match and dp(i-1, j))
                else:
                    match = (s[i] == p[j] or p[j] == ".") and dp(i-1, j-1)
                # print(s[:i+1], p[:j+1], match)
                results[i, j] = match
        return dp(len(s)-1, len(p)-1)


solution = Solution()
print(solution.isMatch("aa", "a"))
print(solution.isMatch("aa", "a*"))
print(solution.isMatch("ab", ".*"))
print(solution.isMatch("aab", "c*a*b"))
print(solution.isMatch("mississippi", "mis*is*p*."))
print(solution.isMatch("mississippi", "mis*is*ip*."))
print(solution.isMatch("a", "ab*a"))
print(solution.isMatch("bbbba", ".*a*a"))
print(solution.isMatch("ab", ".*.."))
print(solution.isMatch("bbaa", "a..."))
print(solution.isMatch("", "c*c*"))
print(solution.isMatch("a", ".*..a*"))
print(solution.isMatch("aaa", "ab*a*c*a"))
