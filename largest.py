class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        normal_order_num = sorted(num)
        if normal_order_num[-1] == 0: # biggest is 0
            return "0"
        as_digit = lambda x, y: cmp(str(x) + str(y), str(y) + str(x))
        new_order = sorted(num, cmp=as_digit, reverse=True)
        largest_str = ''.join([str(i) for i in new_order])
        return largest_str


s = Solution()
l = [0, 0, 0, 0]
print s.largestNumber(l)
