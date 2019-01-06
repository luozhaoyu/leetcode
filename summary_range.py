class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        res = []
        front = None
        end = None
        for i in nums:
            if front == None:
                front = i
            else:
                if end != None:
                    if i == end + 1:
                        end = i
                    elif i > end + 1:
                        res.append("%s->%s" % (front, end))
                        front = i
                        end = None
                else:
                    if i == front + 1:
                        end = i
                    elif i > front + 1:
                        res.append("%s" % front)
                        front = i
                        end = None
        if front != None and end != None:
            res.append("%s->%s" % (front, end))
        elif front != None:
            res.append("%s" % front)

        return res


so = Solution()
l = [
    [],
    [0],
    [1],
    [1, 3],
    [1, 3, 4],
    [1, 2, 3, 4],
    [0, 1, 2, 4, 5, 7]
]

for s in l:
    print s, so.summaryRanges(s)
