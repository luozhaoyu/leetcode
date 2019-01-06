class Solution:
    # @param path, a strin
    # @return a string
    def simplifyPath(self, path):
        paths = path.split('/')
        res = []
        for p in paths:
            if not p or p == ".":
                continue
            elif p == "..":
                if res:
                    res.pop()
            else:
                res.append(p)
        if not res:
            return "/"
        else:
            res.insert(0, '')
            return '/'.join(res)

s = Solution()
ps = [
    "/home/",
    "/a/./b/../../c/",
    "/a/./b/",
    "/a/./b",
    "/home/..",
    "/home/../../..",
    "/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///",
]
for p in ps:
    print p, s.simplifyPath(p)
