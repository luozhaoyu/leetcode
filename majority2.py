class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        if len(nums) % 3 == 0:
            minus = len(nums) / 3 - 1
        else:
            minus = len(nums) / 3
        res = {}
        for i in nums:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
                if len(res) == 3:
                    for k in res.keys():
                        if res[k] == 1:
                            res.pop(k)
                        else:
                            res[k] -= 1
        potential = res.keys()
        for k in res:
            res[k] = 0
        for i in nums:
            if i in potential:
                res[i] += 1
        return [k for k in res if res[k] > len(nums) / 3]

so = Solution()
a = [1] * 10
b = [2] * 10
c = [3] * 7
import random
n = a + b + c + range(11, 13)
random.shuffle(n)
print so.majorityElement(n)
