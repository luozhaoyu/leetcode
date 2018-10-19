import copy

class Board(object):
    def __init__(self, horizontal, vertical, left_oblique, right_oblique, queens, n):
        self.horizontal = horizontal
        self.vertical = vertical
        self.left_oblique = left_oblique
        self.right_oblique = right_oblique
        self.queens = queens
        self.n = n

    def is_valid_position(self, linex, rowj, n):
        if self.horizontal[rowj] != ".":
            return False
        if self.vertical[linex] != ".":
            return False
        if self.left_oblique[(linex + rowj) % (2 * n)] != ".":
            return False
        if self.right_oblique[(linex - rowj) + n] != ".":
            return False
        return True

    def put_here(self, linex, rowj, n):
        self.horizontal[rowj] = "Q"
        self.vertical[linex] = "Q"
        self.left_oblique[(linex + rowj) % (2 * n)] = "Q"
        self.right_oblique[(linex - rowj) + n] = "Q"
        self.queens.append(rowj)

    def __repr__(self):
        return "\n".join(self.output())

    def output(self):
        res = []
        for i in range(len(self.queens)):
            p = ""
            for j in range(self.n):
                if j == self.queens[i]:
                    p += "Q"
                else:
                    p += "."
            res.append(p)
        return res


class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        horizontal = ["."] * n
        vertical = ["."] * n
        left_oblique = ["."] * 2 * n
        right_oblique = ["."] * 2 * n
        queens = []
        board = Board(horizontal, vertical, left_oblique, right_oblique, [], n)
        return self.put_queen(board, n)

    def put_queen(self, board, n):
        """put xth queen on the board"""
        res = []
        if len(board.queens) == n:
            # print(board)
            res.append(board.output())
            return res

        # for the len(queen) queen
        for i in range(n):  # jth queue will sit at jth line
            if board.is_valid_position(len(board.queens), i, n):
                new_board = copy.deepcopy(board)
                new_board.put_here(len(board.queens), i, n)
                res.extend(self.put_queen(new_board, n))
        return res

s = Solution()
print(s.solveNQueens(6))
