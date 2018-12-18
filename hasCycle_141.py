class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #  哈希表
        node_l = set()
        while head :
            if head in node_l:
                return True
            node_l.add(head)
            head = head.next
        return False
        #  龟兔法  双指针

        if head is None or head.next is None:
            return False
        fast = head
        slow = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False