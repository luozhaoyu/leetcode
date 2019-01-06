# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def debug(h):
    res = []
    while h:
        res.append(h.val)
        h = h.next
    s =  "->".join([str(x) for x in res])
    print s
    return s

def generate(l):
    h = ListNode(0)
    current = h
    for i in l:
        n = ListNode(i)
        current.next = n
        current = n
    return h.next

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if k == 0 or not head or not head.next:
            return head
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        k = (length - k % length) % length
        if k == 0:
            return head
        tail = current

        new_head = head
        new_last = None
        for i in range(k):
            if i == k-1:
                new_last = new_head
                new_head = new_head.next
                new_last.next = None
            else:
                new_head = new_head.next
        tail.next = head
        return new_head


so = Solution()
l = [1, 2, 3]
h = generate(l)
debug(h)
debug(so.rotateRight(generate([1, 2]), 2))

