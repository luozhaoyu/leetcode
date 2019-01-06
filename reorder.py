class Solution:

    def reorder(self, node_list):
        i = 0
        while i < (len(node_list) - 1) / 2:
            node_list[i].next = node_list[len(node_list) - i - 1]
            node_list[len(node_list) - i - 1].next = node_list[i + 1]
            i += 1

        if len(node_list) % 2 == 0:
            node_list[i].next = node_list[len(node_list) - i - 1]
            node_list[len(node_list) - i - 1].next = None
        else:
            node_list[i].next = None

    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head:
            return

        node_list = []
        ptr = head
        while ptr:
            node_list.append(ptr)
            ptr = ptr.next
        self.reorder(node_list)

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "%s" % self.val




import copy
s = Solution()
head = ListNode(-1)
ptr = head
for i in range(21000):
    n = ListNode(i)
    ptr.next = n
    ptr = n

print s.reorderList(head)
ptr = copy.copy(head)
while ptr:
    ptr = ptr.next

