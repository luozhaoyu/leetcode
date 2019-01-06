class Symbol(object):
    def __init__(self, value, pre=None, succ=None):
        self.value = value
        self.pre = pre
        self.succ = succ

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        s = s.replace(" ", "")
        head = Symbol(None)
        current = head
        tmp = ""
        highs = []
        lows = []
        for c in s:
            if c.isdigit():
                tmp += c
            else:
                if tmp:
                    s = Symbol(int(tmp), pre=current)
                    current.succ = s
                    current = s
                    tmp = ""
                s = Symbol(c, pre=current)
                current.succ = s
                current = s
                if c == '*' or c == '/':
                    highs.append(s)
                else:
                    lows.append(s)
        if tmp:
            s = Symbol(int(tmp), pre=current)
            current.succ = s
            current = s

        for h in highs:
            if h.value == '*':
                h.pre.value = h.pre.value * h.succ.value
            else:
                h.pre.value = h.pre.value / h.succ.value
            h.pre.succ = h.succ.succ
            if h.succ.succ:
                h.succ.succ.pre = h.pre

        for h in lows:
            if h.value == '+':
                h.pre.value = h.pre.value + h.succ.value
            else:
                h.pre.value = h.pre.value - h.succ.value
            h.pre.succ = h.succ.succ
            if h.succ.succ:
                h.succ.succ.pre = h.pre

        return head.succ.value


so = Solution()
l = [
        "1+1+1",
"1-11",
    "3+2*2",
" 3/2 ",
" 3+5 / 2 ",
"1",
"111",
"111 / 2 + 3 * 3",



]

for s in l:
    print s, so.calculate(s)
