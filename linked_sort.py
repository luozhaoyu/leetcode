class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        ptr = head
        n = 0
        while ptr:
            n += 1
            ptr = ptr.next
        return self.sort(head, n)

    def sort(self, head, length):
        if length <= 1:
            return head

        i = 0
        ptr = head
        while i < length / 2:
            i += 1
            ptr = ptr.next
        left = self.sort(head, i)
        right = self.sort(ptr, length - i)
        left_merged = 0
        right_merged = 0
        head = left if left.val < right.val else right
        current = head
        while left and right and left_merged < i and right_merged < length - i:
            if left.val < right.val:
                current.next = left
                current = left
                left = left.next
                left_merged += 1
            else:
                current.next = right
                current = right
                right = right.next
                right_merged += 1
            #print left_merged, right_merged, i, length - i
            #debug(new_head, left_merged + right_merged + 1)
        while left_merged < i:
            assert left
            current.next = left
            current = left
            left_merged += 1
            if left.next:
                left = left.next
            else:
                break
        while right_merged < length - i:
            assert right
            current.next = right
            current = right
            right_merged += 1
            if right.next:
                right = right.next
            else:
                break
        current.next = None
        print left_merged, right_merged, length, i, length - i
        assert left_merged + right_merged == length
        return head


def debug(ptr, length=0):
    import sys
    n = 0
    while ptr:
        if length and n >= length:
            print
            return
        sys.stdout.write(str(ptr) + ' ')
        ptr = ptr.next
        n += 1
    print


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return "%s" % self.val

s = Solution()
import random
head = ListNode(random.randint(0, 10))
head = ListNode(99)
ptr = head
for i in range(10, 1, -1):
    n = ListNode(i)
    n = ListNode(random.randint(0, 10))
    ptr.next = n
    ptr = n

#head = ListNode(2)
#n = ListNode(1)
#head.next = n
debug(head)
ptr = s.sortList(head)
print "result:"
print id(ptr), ptr.val
debug(ptr)
