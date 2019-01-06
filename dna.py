class Solution:

    def convert_to_int(self, s):
        res = 0
        for c in s:
            res *= 5
            if c == 'A':
                i = 4
            elif c == 'C':
                i = 1
            elif c == 'G':
                i = 2
            else:
                i = 3
            res += i
        return res

    def convert_to_string(self, i):
        s = []
        while i:
            tmp = i % 5
            if tmp == 4:
                s.insert(0, 'A')
            elif tmp == 1:
                s.insert(0, 'C')
            elif tmp == 2:
                s.insert(0, 'G')
            elif tmp == 3:
                s.insert(0, 'T')
            else:
                print "bingo"
            i /= 5
        return ''.join(s)

    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        ints = [self.convert_to_int(s[i * 10: (i+1) * 10]) for i in range(len(s) / 10 + 1)]
        tmp = self.convert_to_int(s[:10])
        string_dict = {tmp: 1}
        result = set()
        for c in s[10:]:
            #: cut only the rest 9 chars
            tmp = tmp % (5 ** 9)
            tmp *= 5
            if c == 'A':
                i = 4
            elif c == 'C':
                i = 1
            elif c == 'G':
                i = 2
            else:
                i = 3
            tmp += i
            if tmp in string_dict:
                string_dict[tmp] += 1
                result.add(tmp)
            else:
                string_dict[tmp] = 1
        output = [self.convert_to_string(i) for i in result]
        return output

s = Solution()
print s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
print s.findRepeatedDnaSequences("AAAAACCCC")
