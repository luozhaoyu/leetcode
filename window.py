class Solution:

    # @return a string

    def minWindow(self, S, T):
        if not S or not T:
            return ''

        count = {}
        for c in T:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

        statistic = {}
        result = {
            'start': 0,
            'end': len(S),
            'covers': [],
        }
        last_positions = {}
        for i, c in enumerate(S):
            if c in T:
                if c in statistic:
                    statistic[c].append(i)
                else:
                    statistic[c] = [i]

                if len(statistic[c]) >= count[c]:
                    last_positions[c] = statistic[c][-count[c]]
                    new_start = min(last_positions.values())
                    if len(statistic[c]) == count[c] or i - new_start < result['end'] - result['start']:
                        result = {
                            'start': new_start,
                            'end': i,
                            'covers': last_positions.keys(),
                        }

        if len(result['covers']) == len(count):
            return S[result['start']: result['end']+1]
        else:
            return ''

so = Solution()
l = [["ADOBECODEBANC", "ABC"],
["a", "b"],
["aa", "aa"],
]
for s, t in l:
    print so.minWindow(s, t)
