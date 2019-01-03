# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #####  method 2
        if head is None or head.next is None:
            return False
        if not head.next.next:
            return head.val == head.next.val
        fast = slow = q = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        def re_list (head):
            if head is None:
                return False
            cur = head
            pre = None
            net = cur.next
            while net:
                cur.next = pre
                pre = cur
                cur = net
                net = net.next
            cur.next = pre
            return cur
        p = ListNode(0)
        p = re_list(slow.next)
        while p.next:
            if p.val != q.val:
                return False
            q = q.next
            p = p.next
        return q.val == p.val



        ####  method 1
        # tem = head
        # tem2 = head
        # list = []
        # len = 0
        # while tem:
        #     len += 1
        #     tem = tem.next
        # for i in range(len//2):
        #     list.append(tem2.val)
        #     tem2 = tem2.next
        # if len%2 == 1:
        #     tem2 = tem2.next
        # while tem2:
        #     if list.pop() == tem2.val:
        #         tem2 = tem2.next
        #     else:
        #         return False
        # return True

s  = Solution()
p1 = ListNode(1)
p2 = ListNode(3)
p3 = ListNode(5)
p4 = ListNode(5)
p5 = ListNode(3)
p6 = ListNode(1)
p7 = ListNode(2)
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p6
p6.next = p7
#
print(s.isPalindrome(p1))


