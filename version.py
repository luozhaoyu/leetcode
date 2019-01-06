class Solution:
    def compareSingle(self, str1, str2):
        if not str1:
            str1 = 0
        if not str2:
            str2 = 0
        v1 = int(str1)
        v2 = int(str2)
        if v1 == v2:
            return 0
        elif v1 > v2:
            return 1
        else:
            return -1
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        vsplit1 = version1.split('.')
        vsplit2 = version2.split('.')
        v1 = 0 if not vsplit1[0] else int(vsplit1[0])
        v2 = 0 if not vsplit2[0] else int(vsplit2[0])
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1
        else:
            if len(vsplit1) == 1:
                res_v1 = ''
            else:
                res_v1 = '.'.join(vsplit1[1:])
            if len(vsplit2) == 1:
                res_v2 = ''
            else:
                res_v2 = '.'.join(vsplit2[1:])
            #print vsplit1, vsplit2

            if not res_v1 and not res_v2:
                return 0
            else:
                return self.compareVersion(res_v1, res_v2)

    
s = Solution()
l = [
    ("10.3", "9.7"),
    ("1.2.3", "1.2"),
    ("7.4", "8.1"),
    ("7.4", "7.4"),
    ("7.4.0", "7.4"),
    ("7.4.0.1", "7.4"),
    ("0.1", "7.4"),
]

for v1, v2 in l:
    print v1, v2, s.compareVersion(v1, v2)
