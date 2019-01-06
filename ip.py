import copy
class Solution:

    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        if not s:
            return []
        res = set()
        queue = [[]]
        while queue:
            q = queue.pop(0)
            len_q = sum([len(i) for i in q]) if q else 0
            if len(q) == 4:
                if len_q == len(s):
                    #res.add(".".join(["%s" % int(i) for i in q]))
                    res.add(".".join(q))
            else:
                n = 1
                new_combine = s[len_q: len_q+n]
                try:
                    while (len_q + n) <= len(s) and 0 <= int(new_combine) and int(new_combine) <= 255 and new_combine == "%s" % int(new_combine):
                        new_q = copy.copy(q)
                        new_q.append(new_combine)
                        queue.append(new_q)
                        n += 1
                        new_combine = s[len_q: len_q+n]
                except:
                    print q, new_combine, len_q, len_q + n, len(s)
                    raise
        return list(res)

s = Solution()
for ip in ["25525511135", "0000", "010010"]:
    print s.restoreIpAddresses(ip)
