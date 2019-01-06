class Solution:

    # @param s, a string

    # @return an integer

    def minCut(self, s):
        if not s:
            return 0

        pal = []
        dp = []
        for i in range(len(s)):
            t = [None] * len(s)
            t[i] = True
            pal.append(t)
            dp.append(i+1)

        for k in range(1, len(s)):
            dp[k] = min(dp[k], dp[k - 1] + 1)
            for i in range(1, k+1):
                if i == 1:
                    if s[k-1] == s[k]:
                        pal[k-1][k] = True
                        if k == 1:
                            dp[1] = 1
                        else:
                            dp[k] = min(dp[k], 1 + dp[k-2])
                elif i == k:
                    if s[0] == s[k]:
                        pal[0][k] = pal[1][k-1]
                        if pal[0][k]:
                            dp[k] = 1
                    else:
                        pal[0][k] = False
                else:
                    if s[k - i] == s[k]:
                        pal[k-i][k] = pal[k-i+1][k-1]
                        if pal[k-i][k]:
                            #print s[k-i: k+1]
                            dp[k] = min(dp[k], 1 + dp[k-i-1])
                    else:
                        pal[k-i][k] = False
                #print k-i, k, pal[k-i][k], s[k-i: k+1], dp[k]
        #print dp
        return dp[-1] - 1

so = Solution()
l = [
'aab',
'abcddcbaxyx',
'axxycyk',
'abc',
'abcddcba',
"apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
,
]
for i in l:
    print i, len(i)
    print so.minCut(i)
