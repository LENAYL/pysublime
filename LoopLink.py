# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead is None:
            return None
        node1 = self.Meeting(pHead)
        if node1 is None:
            return None
        count = 1
        while node1.next != self.Meeting(pHead):
            node1 = node1.next
            count += 1
        node2 = pHead
        for i in range(count):
            node2 = node2.next
        node1 = pHead
        while node1 != node2:
            node1 = node1.next
            node2 = node2.next
        return node2

    def Meeting(self,pHead):
        slow = pHead.next
        if slow is None:
            return None
        fast = slow.next
        while fast != None and slow != None:
            if slow == fast:
                return fast
            slow = slow.next
            fast = fast.next
            if fast != None:
                fast = fast.next
        return None