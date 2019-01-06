class Solution:

    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                stop = False
                for i in range(len(stack) - 1, -1, -1):
                    if isinstance(stack[i], int):
                        continue
                    elif stack[i] == '(':
                        stack[i] = 2
                        stop = True
                        break
                    elif stack[i] == ')':
                        stack.append(')')
                        stop = True
                        break
                if not stop:
                    stack.append(')')
        tmp = 0
        max_parentheses = 0
        for i in stack:
            if isinstance(i, int):
                tmp += i
            else:
                if tmp > max_parentheses:
                    max_parentheses = tmp
                tmp = 0
        if tmp > max_parentheses:
            max_parentheses = tmp
        return max_parentheses

s = Solution()
for w in [")()())", "(()", "()(()", "()"]:
    print w, s.longestValidParentheses(w)

