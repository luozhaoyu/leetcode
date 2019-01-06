class Solution:

    # @param s, a string

    # @return an integer

    def numDecodings(self, s):
        if not s:
            return 0
        if s[0] == '0':
            return 0

        f = [1]
        i = 1
        while i < len(s):
            code = int(s[i-1] + s[i])
            if code == 0:
                return 0
            elif code % 10 == 0:
                if code >= 30:
                    return 0
                if i > 1:
                    f.append(f[i-2])
                else:
                    f.append(1)
            elif code <= 9:
                f.append(f[i-1])
            elif code <= 26:
                if i>1:
                    f.append(f[i - 1] + f[i - 2])
                else:
                    f.append(f[i-1] + 1)
            else:
                f.append(f[i-1])
            i += 1
        return f[-1]

s = Solution()
print s.numDecodings("230")
print s.numDecodings("110")
print s.numDecodings("1212")
print s.numDecodings("1212123")
print s.numDecodings("0")
print s.numDecodings("101212")
print s.numDecodings("1001212")
