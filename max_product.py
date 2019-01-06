class Solution:

    # @param A, a list of integers

    # @return an integer

    def maxProduct(self, A):
        max_ = None
        min_ = None
        result = A[0]
        for i in A:
            if i > 0:
                max_ = max(i, i * max_) if max_ else i
                min_ = min(i, i * min_) if min_ else i
            elif i < 0:
                t = max_
                max_ = max(i, min_ * i) if max_ else i
                min_ = min(i, t * i) if min_ else i
            else:
                max_ = 0
                min_ = 0
            if max_ > result:
                result = max_
        return result

s = Solution()
print s.maxProduct([2, 3, -2, 4, 2, 2, 2, -7, 2, -10])
print s.maxProduct([2, -1, 0, 1, 2])
print s.maxProduct([-1, 0, 1, 2])
print s.maxProduct([3, 0, -1, 4])
print s.maxProduct([-1])
print s.maxProduct([-2, 0, -1])

