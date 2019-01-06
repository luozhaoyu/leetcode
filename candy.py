class Solution:
    def cal(self, count):
        if len(count) == 1:
            return 1

        total = 0
        for i, c in enumerate(count):
            if c == 'max':
                if i == 0:
                    if count[i+1] == 'min':
                        total += 2
                    else:
                        total += 2 + count[i+1]
                elif i == len(count) - 1:
                    if count[i-1] == 'min':
                        total += 2
                    else:
                        total += 2 + count[i-1]
                else:
                    t = [0]
                    if count[i-1] != 'min':
                        t.append(count[i-1])
                    if count[i+1] != 'min':
                        t.append(count[i+1])
                    total += 2 + max(t)
            elif c == 'min':
                total += 1
            else:
                total += (3 + c) * c / 2
        #print count, total
        return total

    # @param ratings, a list of integer

    # @return an integer

    def candy(self, ratings):
        if not ratings:
            return 0
        if len(ratings) == 1:
            return 1
        elif len(ratings) == 2:
            if ratings[0] == ratings[1]:
                return 2
            else:
                return 3

        count = []
        for i, r in enumerate(ratings):
            if i == 0:
                if ratings[i] <= ratings[i+1]:
                    count.append('min')
                elif ratings[i] > ratings[i+1]:
                    count.append('max')
            elif i == len(ratings) - 1:
                if ratings[i] <= ratings[i-1]:
                    count.append('min')
                elif ratings[i] > ratings[i-1]:
                    count.append('max')
            else:
                if r == ratings[i-1]:
                    return self.cal(count) + self.candy(ratings[i:])

                if r > ratings[i-1] and r >= ratings[i+1]:
                    count.append('max')
                elif r < ratings[i-1] and r <= ratings[i+1]:
                    count.append('min')
                else:
                    if isinstance(count[-1], int):
                        count[-1] += 1
                    else:
                        count.append(1)
        return self.cal(count)

        for i, r in enumerate(ratings):
            if i == 0:
                current = ratings[0]
                total = current
                minimum = current
                continue

            if ratings[i] > ratings[i-1]:
                current += 1
                total += current
            elif ratings[i] < ratings[i-1]:
                current -= 1
                total += current
                if current < minimum:
                    minimum = current
            else:
                total += (1 - minimum) * i + self.candy(ratings[i:])
                return total
            print total, minimum

        total += len(ratings) * (1 - minimum)
        return total

s = Solution()
l = [
[0.1],
[1, 0, 1, 2, 0, -1, 3, -3, 3],
[1, 2, 2],
[2, 2],
[2, 2, 2, 2, 2, 2],
[5, 5, 5, 3, 3, 2],
[4,2,3,4,1],
range(12000)[::-1],
]

for r in l:
    print r
    print s.candy(r)
