class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        if num1 == '0' or num2 == '0':
            return '0'

        num1 = num1[::-1]
        num2 = num2[::-1]
        res = [0] * (len(num1) + len(num2) + 2)
        for j, m in enumerate(num2):
            for i, n in enumerate(num1):
                m = int(m)
                n = int(n)
                multiply = m * n
                res[i+j] += multiply
                increase = res[i+j] / 10
                res[i+j] %= 10
                k = 1
                while increase:
                    res[i+j+k] += increase
                    increase = res[i+j+k] / 10
                    res[i+j+k] %= 10
                    k += 1
        return ''.join(["%s" % i for i in res]).rstrip('0')[::-1]


s = Solution()
import random
a = random.randint(1, 10000000)
b = random.randint(1, 1000000000000)
c = s.multiply("%s" % a, "%s" % b)
print a, b, c, a*b
assert int(c) == a * b
