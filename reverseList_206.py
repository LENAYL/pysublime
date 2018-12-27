# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        cur = head
        pre =None
        temp = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
        # method 1
        # if head is None:
        #     return None
        # pre = head
        # cur = head.next
        # pre.next = None
        # while pre and cur:
        #
        #     temp = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = temp
        # return pre
s = Solution()
p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p5 = ListNode(5)
p6 = ListNode(6)
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p6
a = s.reverseList(p1)
while a :
    print(a.val)
    a = a.next

# print(s.reverseList(p1))



        # count = 0
        # dict = {0: head.val}
        # while temp and temp.next:
        #     # if temp.next:
        #     count += 1
        #     dict[count] = temp.val
        #     temp = temp.next
        # count += 1
        # dict[count] = temp.val
        # for i in range(count//2 +1):
        #     t = dict[i]
        #     dict[i] = dict[count-1-i]
        #     dict[count - 1 - i] = t


