class Solution:
    # @return a string
    def convertToTitle(self, num):
        res = []
        while num:
            res.insert(0, num % 26)
            num /= 26
        i = len(res) - 1
        is_short = False
        while i >= 0:
            if res[i] == 0:
                res[i] = 26
                is_short = True
            else:
                if is_short:
                    if res[i] == 1:
                        res[i] = 26
                    else:
                        res[i] -= 1
                        is_short = False
            i -= 1
        if is_short:
            res.pop(0)

        s = ''
        for i in res:
            s += chr(ord('A') + i - 1)
        return s

s = Solution()
print s.convertToTitle(3)
print s.convertToTitle(26)
print s.convertToTitle(28)
print s.convertToTitle(2 * 26 ** 2)
print s.convertToTitle(702)

