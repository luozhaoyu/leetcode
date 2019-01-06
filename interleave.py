class Solution:

    # @return a boolean

    def isInterleave(self, s1, s2, s3):
        if len(s3) != len(s1) + len(s2):
            return False
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        f = []
        for i in range(len(s3)+1):
            f.append([None] * (len(s3)+1))
        f[0][0] = True
        for k in range(1, len(s3)+1): # the total length
            min_s1 = max(k-len(s2), 0)
            max_s1 = min(len(s1), k)
            for i in range(min_s1, max_s1+1):
                if i == 0:
                    f[0][k] = (s3[k-1] == s2[k-1] and f[0][k-1])
                elif k - i == 0:
                    f[k][0] = (s3[k-1] == s1[k-1] and f[k-1][0])
                else:
                    f[i][k-i] = (s3[k-1] == s1[i-1] and f[i-1][k-i]) or\
                        (s3[k-1] == s2[k-i-1] and f[i][k-i-1])
                #print i, k-i, f[i][k-i]
        return f[len(s1)][len(s2)]


s = Solution()
l = [
["aabcc", "dbbca", "aadbbcbcac"],
["aabcc", "dbbca", "aadbbbaccc"],
["azb", "czd", "aczybd"],
["azb", "czd", "aczzbd"],
["", "", ""],
["a", "a", "aa"],
["aabd", "abdc", "aabdabcd"],
["a", "", "c"],
["aa", "ab", "abaa"],
]

for s1, s2, s3 in l:
    print s.isInterleave(s1, s2, s3)
