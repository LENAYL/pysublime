class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA and headB:
            # node_n = []
            node_A = headA
            node_B = headB
            if node_B.next == node_A and node_A.next == node_B:
                return 'Intersected at ' and node_B.val
            ta = 1
            tb = 1
            while node_A.next:
                ta += 1
                node_A = node_A.next
            while node_B.next:
                tb += 1
                node_B = node_B.next
            if node_B.val == node_A.val:
                node_A = headA
                node_B = headB
                # return 'Intersected at ' and node_B.val
                while ta > tb:
                    ta -= 1
                    node_A = node_A.next
                while ta < tb:
                    tb -= 1
                    node_B = node_B.next
                while node_A and node_B:
                    if node_A == node_B:
                        return 'Intersected at ' and node_B.val
                    node_A = node_A.next
                    node_B = node_B.next












                    # while node_A:
            #     node_n.append(node_A)
            #     node_A = node_A.next
            # while node_B:
            #     if node_B in node_n:
            #         # print('Intersected at '(node_B.val))
            #         # break
            #         return 'Intersected at ' and node_B.val
            #     else:
            #         node_B = node_B.next
s  = Solution()
p1 = ListNode(1)
p2 = ListNode(3)
p3 = ListNode(8)
p4 = ListNode(7)
p5 = ListNode(2)
# p6 = ListNode(9)
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
# p5.next = p6

p7 = ListNode(1)
# p8 = ListNode(2)
# p9 = ListNode(2)
# p_1 = ListNode(8)
# p_2 = ListNode(7)
# p_3 = ListNode(8)

# p1.next = p7
p7.next = p3
# p8.next = p3
# p9.next = p3
# p8.next = p9
print(s.getIntersectionNode(p1, p7))

