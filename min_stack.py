class MinStack:
    def __init__(self):
        self.data = []
        self.head_small = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.data.append(x)
        if not self.head_small:
            self.head_small.append([x, 1])
        elif x < self.getMin():
            self.head_small.insert(0, [x, 1])
        elif x == self.getMin():
            self.head_small[0][1] += 1

    # @return nothing
    def pop(self):
        p = self.data.pop()
        if p == self.getMin():
            if self.head_small[0][1] == 1:
                self.head_small.pop(0)
            else:
                self.head_small[0][1] -= 1

    # @return an integer
    def top(self):
        return self.data[-1]

    # @return an integer
    def getMin(self):
        return self.head_small[0][0]

s = MinStack()
import random
s.push(3)
s.push(1)
s.push(2)
s.push(0)
print s.getMin()
s.pop()
print s.getMin()
