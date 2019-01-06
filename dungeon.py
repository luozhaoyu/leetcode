class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        f = []
        for i in range(m):
            f.append([(None, None)] * n)
        f[0][0] = (min(0, dungeon[0][0]), dungeon[0][0])
        try:
            for step in range(1, m + n - 1):
                for i in range(m):
                    if i >=0 and i < m and step - i < n and step - i >= 0:
                        #print i, step - i
                        if i == 0:
                            final_hp = f[i][step-i-1][1] + dungeon[i][step - i]
                            if final_hp < 0:
                                f[i][step - i] = (f[i][step-i-1][0] - final_hp, 0)
                            else:
                                f[i][step - i] = (f[i][step-i-1][0], final_hp)
                        elif step - i == 0:
                            final_hp = f[i-1][step-i][1] + dungeon[i][step - i]
                            if final_hp < 0:
                                f[i][step - i] = (f[i-1][step-i][0] - final_hp, 0)
                            else:
                                f[i][step - i] = (f[i-1][step-i][0], final_hp)
                        else:
                            health_i = f[i-1][step-i][1] + dungeon[i][step-i]
                            if health_i < 0:
                                need_i = f[i-1][step-i][0] - health_i
                                health_i = 0
                            else:
                                need_i = f[i-1][step-i][0]
                            health_j = f[i][step-i-1][1] + dungeon[i][step-i]
                            if health_j < 0:
                                need_j = f[i][step-i-1][0] - health_j
                                health_j = 0
                            else:
                                need_j = f[i][step-i-1][0]

                            if need_i < need_j:
                                f[i][step - i] = (need_i, health_i)
                            elif need_i > need_j:
                                f[i][step - i] = (need_j, health_j)
                            else:
                                if health_i > health_j:
                                    f[i][step - i] = (need_i, health_i)
                                else:
                                    f[i][step - i] = (need_j, health_j)
        except (IndexError, TypeError):
            print f
            print step, i, step-i
            raise
        print f
        return max(1 - f[m-1][n-1][0], 1)

s = Solution()
d = [
    [1, -3, 3],
    [0, -2, 0],
    [-3, -3, -3]
]
print s.calculateMinimumHP(d)
