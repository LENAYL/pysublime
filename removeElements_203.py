# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        node = ListNode(0)
        node.next = head
        temp = node
        while temp and temp.next and temp.next.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        if temp is None:
            return False
        elif temp.next is None:
            if temp.val == val:
                temp = None

        else:

            if temp.next.val == val:
                temp.next = None
        return node.next


s  = Solution()
p1 = ListNode(3)
p2 = ListNode(3)
p3 = ListNode(5)
p4 = ListNode(7)
p5 = ListNode(3)
p6 = ListNode(3)
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p6
val = 3
print(s.removeElements(p1, val))

