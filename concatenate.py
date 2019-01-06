import copy
class Solution:

    # @param S, a string

    # @param L, a list of string

    # @return a list of integer

    def findSubstring(self, S, L):
        if not S or not L:
            return []

        total_l = len(L) * len(L[0])
        result = []
        count = {}
        for w in L:
            if w in count:
                count[w] += 1
            else:
                count[w] = 1

        for i in range(len(L[0])):
            j = i
            init_str = S[j: j+total_l]
            if len(init_str) < total_l:
                break

            l_copy = copy.copy(L)
            matches = {}
            k = 0
            while k + len(L[0]) <= len(init_str):
                w = init_str[k: k+len(L[0])]
                #print w
                if w in L:
                    if w in matches:
                        matches[w] += 1
                    else:
                        matches[w] = 1
                k += len(L[0])
            if matches == count:
                result.append(i)

            #print init_str, matches
            j += len(L[0])
            while j + total_l <= len(S):
                old_str = S[j-len(L[0]): j]
                new_str = S[j + total_l - len(L[0]): j + total_l]
                if old_str in matches.keys():
                    matches[old_str] -= 1
                if new_str in L:
                    if new_str in matches:
                        matches[new_str] += 1
                    else:
                        matches[new_str] = 1

                #print S[j: j+total_l], old_str, new_str, matches
                if matches == count:
                    result.append(j)
                j += len(L[0])
        return result

so = Solution()

L = [
["barfoothefoobarman", ["foo", "bar"]],
["barfoothefoobarmanfo", ["foo", "bar"]],
["a", ["a"]],
["lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]],
["abababab", ["a","b","a"]],
]
for s, l in L:
    print so.findSubstring(s, l)
