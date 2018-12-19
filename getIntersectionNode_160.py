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
        #  method 1   哈希表  将其中一个链表存入dict   遍历后面的链表  出现相同key 返回value
        node1 = headA
        node2 = headB
        dict = {}
        while node1:
            dict[node1] = node1.val
            node1 = node1.next
        while node2:
            if node2 in dict:
                return 'Intersected at ' and dict[node2]
            node2 = node2.next






        #   method 2
        #   链表尾部是否相等  相等即相交  否则直接无输出 结束
        #   相交：分为以下几个步骤：
        #   1、将长链表的长度缩短至和短链表一样   从头开始遍历 直到两者相等 即为相交节点

        # if headA and headB:
        #     # node_n = []
        #     node_A = headA
        #     node_B = headB
        #     if node_B.next == node_A and node_A.next == node_B:
        #         return 'Intersected at ' and node_B.val
        #     ta = 1
        #     tb = 1
        #     while node_A.next:
        #         ta += 1
        #         node_A = node_A.next
        #     while node_B.next:
        #         tb += 1
        #         node_B = node_B.next
        #     if node_B.val == node_A.val:
        #         node_A = headA
        #         node_B = headB
        #         # return 'Intersected at ' and node_B.val
        #         while ta > tb:
        #             ta -= 1
        #             node_A = node_A.next
        #         while ta < tb:
        #             tb -= 1
        #             node_B = node_B.next
        #         while node_A and node_B:
        #             if node_A == node_B:
        #                 return 'Intersected at ' and node_B.val
        #             node_A = node_A.next
        #             node_B = node_B.next












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

