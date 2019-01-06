import copy

def is_neighbor(a, b):
    if a == b:
        return False
    return (a[0] == b[0] or a[1] == b[1]) and abs(a[0] + a[1] - b[0] - b[1]) == 1

class Paths:
    def __init__(self, path):
        self.path = [path]

    def is_neighbor(self, point):
        return is_neighbor(self.path[-1], point)

    def __str__(self):
        return "%s" % self.path

class Solution:

    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        char_info = {}
        for i, l in enumerate(board):
            if isinstance(l, list):
                s = l[0]
            else:
                s = l
            for j, c in enumerate(s):
                if c in char_info:
                    char_info[c].append((i, j))
                else:
                    char_info[c] = [(i, j)]

        if word[0] not in char_info:
            return False
        queue = [Paths(pair) for pair in char_info[word[0]]]
        for c in word[1:]:
            if not queue or c not in char_info:
                return False

            new_queue = []
            for q in queue:
                for point in char_info[c]:
                    if point not in q.path and q.is_neighbor(point):
                        new_q = copy.deepcopy(q)
                        new_q.path.append(point)
                        new_queue.append(new_q)
            queue = new_queue
        if queue:
            return True
        else:
            return False

s = Solution()
board = [
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
words= ["ABCCED", "SEE", "ABCB"]
for w in words:
    print w, s.exist(board, w)

print s.exist(["a"], "ab")
print s.exist(["a"], "b")
print s.exist(["aa"], "aa")
print s.exist(["ab", "cd"], "acdb")
