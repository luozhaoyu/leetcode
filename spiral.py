class Solution:

    def spiral(self, matrix, direction):
        if not matrix or not matrix[0]:
            return []

        direction += 1
        if direction % 4 == 0: # right
            return matrix[0] + self.spiral(matrix[1:], direction)
        elif direction % 4 == 1: # down
            new = [i[-1] for i in matrix]
            matrix = [i[:len(i)-1] for i in matrix]
            return new + self.spiral(matrix, direction)
        elif direction % 4 == 2: # left
            return matrix[-1][::-1] + self.spiral(matrix[:len(matrix)-1], direction)
        elif direction % 4 == 3: # up
            new = [i[0] for i in matrix][::-1]
            matrix = [i[1:] for i in matrix]
            return new + self.spiral(matrix, direction)

    # @param matrix, a list of lists of integers
    # @return a list of integer
    def spiralOrder(self, matrix):
        tmp = self.spiral(matrix, -1)
        return tmp

s = Solution()
m = [[7],[9],[6]]
m = []
m = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
m = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

print s.spiralOrder(m)
