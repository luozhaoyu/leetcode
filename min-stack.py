class MinStack:
    def __init__(self):
        self.data = []
        #: store the index of data, so the value need to be referred by data
        self.heap = []

    def get_value(self, i):
        return self.data[self.heap[i]]

    def get_left_value(self, i):
        return self.data[self.heap[i * 2 + 1]]

    def get_right_value(self, i):
        return self.data[self.heap[i * 2 + 2]]

    def get_parent_value(self, i):
        return self.data[self.heap[(i-1) / 2]]

    def has_left_child(self, i):
        return i * 2 + 1 <= len(self.heap) - 1

    def has_right_child(self, i):
        return i * 2 + 2 <= len(self.heap) - 1

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.data.append(x)
        new_index = len(self.data) - 1
        self.heap.append(new_index)
        cursor = new_index
        while cursor:
            # less than father
            if self.get_value(cursor) < self.get_parent_value(cursor):
                self.heap[cursor], self.heap[(cursor-1) / 2] = self.heap[(cursor-1) / 2], self.heap[cursor]
                cursor = (cursor - 1) / 2
            else:
                break
        return x


    # @return nothing
    def pop(self):
        popped_index = len(self.data) - 1
        self.data.pop()
        heap_index = self.heap.index(popped_index)
        cursor = heap_index
        while self.has_left_child(cursor):
            if self.has_right_child(cursor):
                if self.get_left_value(cursor) < self.get_right_value(cursor):
                    self.heap[cursor] = self.heap[cursor * 2 + 1]
                    cursor = cursor * 2 + 1
                else:
                    self.heap[cursor] = self.heap[cursor * 2 + 2]
                    cursor = cursor * 2 + 2
            else:
                self.heap[cursor] = self.heap[cursor*2 + 1]
                cursor = cursor * 2 + 1
        self.heap.pop() # last one is useless

    # @return an integer
    def top(self):
        return self.data[0]

    # @return an integer
    def getMin(self):
        return self.data[self.heap[0]]

    def __str__(self):
        return "%s %s" % (self.data, [self.data[i] for i in self.heap])

s = MinStack()
import random
for i in range(-10000, 0):
    #s.push(random.randint(0, 50))
    s.push(i)

for i in range(3):
    s.pop()
print s.data, s.head_small
