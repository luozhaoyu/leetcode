#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    surrounded_regions.py
    ~~~~~~~~~~~~~~

    A brief description goes here.
"""
class Solution:

    # @param board, a 2D array

    # Capture all regions by modifying the input board in-place.

    # Do not return any value.

    def solve(self, board):
        def get_boundary_zero(board):
            """
                Returns:
                    [i, j] -> list of "i+j"
            """
            zeros = set()
            for i, c in enumerate(board[0]):
                if c == 'O':
                    zeros.add('0+%d' % i)
            for i, c in enumerate(board[-1]):
                if c == 'O':
                    zeros.add('%d+%d' % (len(board) - 1, i))

            for i in range(0, len(board)):
                l = len(board[i]) - 1
                if board[i][0] == 'O':
                    zeros.add('%d+0' % i)
                if board[i][l] == 'O':
                    zeros.add('%d+%d' % (i, l))
            return zeros

        def get_all_zeros(board):
            zeros = set()
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 'O':
                        zeros.add("%d+%d" % (i, j))
            return zeros


        if not board:
            return []

        all_zeros = get_all_zeros(board)
        boundary_zeros = get_boundary_zero(board)

        queue = list(boundary_zeros)
        while queue:
            x, y = queue.pop().split('+')
            x = int(x)
            y = int(y)
            if x > 0 and board[x - 1][y] == 'O' and not "%d+%d" % (x-1, y) in boundary_zeros:
                queue.append("%d+%d" % (x-1, y))
            if x < len(board) - 1 and board[x + 1][y] == 'O' and not "%d+%d" % (x+1, y) in boundary_zeros:
                queue.append("%d+%d" % (x+1, y))
            if y > 0 and board[x][y-1] == 'O' and not "%d+%d" % (x, y-1) in boundary_zeros:
                queue.append("%d+%d" % (x, y-1))
            if y < len(board[0]) - 1 and board[x][y+1] == 'O' and not "%d+%d" % (x, y+1) in boundary_zeros:
                queue.append("%d+%d" % (x, y+1))
            boundary_zeros.add("%d+%d" % (x, y))
        for i in (all_zeros - boundary_zeros):
            x, y = i.split('+')
            x = int(x)
            y = int(y)
            tmp = [i for i in board[x]]
            tmp[y] = 'X'
            board[x] = ''.join(tmp)
        return board


def main(argv):
    s = Solution()
    boards = [
        ["XXX",
        "XOX",
        "XXX"],
        [
        "XXXOX",
        "XOOOX",
        "XXOXX",
        "XOXOX",
        "XOXXX",
        ],
        [],
        ]
    def mprint(l):
        for i in l:
            print i

    import time
    for b in boards:
        print len(b)
        if b:
            print len(b[0])
        t1 = time.time()
        s.solve(b)
        t2 = time.time()
        print t2 - t1


if __name__ == '__main__':
    import sys
    main(sys.argv)
