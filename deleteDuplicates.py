# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        # temp = ListNode(0)
        temp = head
        while temp.next is not None:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head


s = Solution()
a = ListNode(1)

b = ListNode(1)
c = ListNode(2)
d = ListNode(3)
e = ListNode(3)
f = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# d = [a, b, c]
# a=[1,1,2]
print(s.deleteDuplicates((ListNode([1,1,1,2,3,4]))))
# print((a.next.next.val))