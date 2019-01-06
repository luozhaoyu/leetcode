class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num.sort()
        digit_count = {}
        sum_count = {}
        for i in num:
            if i in digit_count:
                digit_count[i] += 1
            else:
                digit_count[i] = 1

        for i in range(len(num)-1):
            for j in range(i+1, len(num)):
                sum2 = num[i] + num[j]
                if sum2 in sum_count:
                    sum_count[sum2].add((num[i], num[j]))
                else:
                    sum_count[sum2] = set([(num[i], num[j])])
        sum_count_keys = sum_count.keys()
        sum_count_keys.sort()

        res = set([])
        for sum2 in sum_count:
            if target - sum2 in sum_count:
                for t1 in sum_count[sum2]:
                    for t2 in sum_count[target-sum2]:
                        tmp = [t1[0], t1[1], t2[0], t2[1]]
                        tmp.sort()
                        tmp_count = {}
                        for j in tmp:
                            if j in tmp_count:
                                tmp_count[j] += 1
                            else:
                                tmp_count[j] = 1
                        valid = True
                        for j in tmp_count:
                            if tmp_count[j] > digit_count[j]:
                                valid = False
                                break
                        if valid:
                            res.add(tuple(tmp))
        return [list(i) for i in res]


s = Solution()
num = [1]
num = []
num = [1, 0, -1, 0, -2, 2]
num = [1,-2,-5,-4,-3,3,3,5]
target = -11
print s.fourSum(num, target)
