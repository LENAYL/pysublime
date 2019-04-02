# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None
# #
# # class Solution:
# #     def deleteDuplicates(self, head):
# #         """
# #         :type head: ListNode
# #         :rtype: ListNode
# #         """
# #         # try:
# #         #     l1 = head
# #         #     l2 = head.next
# #         #     if l2.next == None:
# #         #         if l1.val == l2.val:
# #         #             return l2
# #         #         else:
# #         #             return l1
# #         #     p1 = l1
# #         #     p2 = l2
# #         #     newnode = ListNode(0)
# #         #     new = newnode
# #         #     flag = 0
# #         #     while p1 is not None and p2 is not None:
# #         #         if p1.val != p2.val:
# #         #             new.next = p1
# #         #             p1 = p2
# #         #             p2 = p2.next
# #         #             new = new.next
# #         #             flag = 1
# #         #         else:
# #         #             p2 = p2.next
# #         #     if flag == 0:
# #         #         p1.next = None
# #         #         return p1
# #         #     if p1 == None:
# #         #         new.next.val = p2.val
# #         #     if p2 == None:
# #         #         new.next.val = p1.val
# #         #     new.next.next = None
# #         #     return newnode.next
# #         # except:
# #         #     return head
# #         if head is None:
# #             return None
# #         # temp = ListNode(0)
# #         temp = head
# #         while temp.next is not None:
# #             if temp.val == temp.next.val:
# #                 temp.next = temp.next.next
# #             else:
# #                 temp = temp.next
# #         return head
# #
# #
# # p1 = ListNode(1)
# # p2 = ListNode(1)
# # p3 = ListNode(1)
# # p4 = ListNode(3)
# # p5 = ListNode(4)
# # p6 = ListNode(4)
# # p1.next = p2
# # p2.next = p3
# # p3.next = p4
# # p4.next = p5
# # p5.next = p6
#
# # s = Solution()
# # p = s.deleteDuplicates(p1)
# # while p != None:
# #     print(p.val)
# #     p = p.next
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         newnode = ListNode(0)
#         new = newnode
#         if l1 is None:
#             return l2
#         if l2 is None:
#             return l1
#         p1 = l1
#         p2 = l2
#         while p1 is not None and p2 is not None:
#             if p1.val < p2.val:
#                 new.next = p1
#                 p1 = p1.next
#             else:
#                 new.next = p2
#                 p2 = p2.next
#             new = new.next
#         # else:
#         #     if p1 is None:
#         #         new.next = l2
#         #     if p2 is None:
#         #         new.next = l1
#
#         if p1 == None:
#             new.next = p2
#         elif p2 == None:
#             new.next = p1
#         return newnode.next
# s  = Solution()
# # p1 = ListNode(1)
# # p2 = ListNode(3)
# p3 = ListNode(5)
# p4 = ListNode(7)
# p5 = ListNode(8)
# p6 = ListNode(9)
# # p1.next = p2
# # p2.next = p3
# p3.next = p4
# p4.next = p5
# p5.next = p6
#
# p7 = ListNode(1)
# p8 = ListNode(2)
# p9 = ListNode(2)
#
# p7.next = p8
# p8.next = p9
#
# # print((s.mergeTwoLists(ListNode([1, 2, 4, 6]), ListNode([1, 3, 5, 7]))))
# # p = s.deleteDuplicates(p1)
# # p = s.mergeTwoLists(ListNode([1, 2, 4, 6]), ListNode([1, 3, 5, 7]))
# p = s.mergeTwoLists(p3, p7)
# # print((s.mergeTwoLists(p3, p7)))
# while p != None:
#     print(p.val)
#     p = p.next
# list_1 = []
# list_1.append([2] + [1])
# list_2 = [1]
# list_2.append(list_1)
# print(list_1)
# print(list_2[1][1])
# for i in range(1,2):
#     print(i)
# from scipy.special import comb
# import math
# a = [x for x in range(31+1)]
# b = [31]*32
# c = []
# for i in range(len(a)):
#     c.append(math.ceil(comb(b[i], a[i])))
# print(c)
# l = [1,3,4,2,2,5]
# del l[2]
# print(l)
# # l.pop(l.index(min(l)))
# # # del l[1]
# s = "A man, a plan, a canal: Panama"
# s = filter(str.isalnum, s)
# s = list(s)
# print(s)
# l = [i.upper()  for i in s]
# print( l)
# print(l.pop().lower())
# print(l)
# print(s.lower())
# print(s[5])
# from queue import Queue

# 如果maxsize设置为小于0或者不设置，队列为无限长
# que = Queue(maxsize=2)

# 进队列
# que.put(1)

# 出队列
# result = que.get()
# s = '78013456789'
# print(s[6:9])
# s = [1,5,8,4,6,0,7,9]
# s = set([4,7,2,5])
# print(s)
# print(s.pop())
# print(s.index(min(s)))
# for i in [12.123011, 12.10, 200.02333000, 200.0]:
#     '{:g}'.format(i)
    # print(i)
# print(pow(8, 1/2))
# astr = 'go o d'
# print(id(astr))
# print(' '.join(astr))
# astr += 'aa'
# print(id(astr))
# def quickSort(array):
#     if len(array) < 2:  # 基线条件（停止递归的条件）
#         return array
#     else:  # 递归条件
#         baseValue = array[0]  # 选择基准值
#         less, equal, greater = [], [baseValue], []
#         for m in array[1:]:
#             if m < baseValue:
#                 # 由所有小于基准值的元素组成的子数组
#                 less.append(m)
#             elif m > baseValue:
#                 # 由所有大于基准值的元素组成的子数组
#                 greater.append(m)
#             else:
#                 # 包括基准在内的同时和基准相等的元素，在上一个版本的百科当中，并没有考虑相等元素
#                 equal.append(m)
#         return quickSort(less) + equal + quickSort(greater)
# # 示例：
# array = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
# print(quickSort(array))
# # 输出为[1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 9, 9, 10, 12, 15, 15, 17]
# str1 = "this is really a string example....wow!!!"
# str2 = "is"
# print(ord('q'))
#
# print (str1.rfind(str2))
#
# print (str1.rfind(str2, 0, 10))
# print (str1.rfind(str2, 10, 0))
#
# print (str1.find(str2))
# print (str1.find(str2, 0, 10))
# print (str1.find(str2, 10, 0))
# s1 = "-"
# s2 = ""
# seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
# print (s1.join( seq ))
# print (type(s2.join( seq )))
# root = TreeNode(1)
# one_1 = TreeNode(2)
# one_2 = TreeNode(2)
# two_1 = TreeNode(3)
# two_2 = TreeNode(4)
# two_3 = TreeNode(4)
# two_4 = TreeNode(3)
# three_1 = TreeNode(5)
# three_2 = TreeNode(6)
# three_3 = TreeNode(7)
# three_4 = TreeNode(8)
# three_5 = TreeNode(8)
# three_6 = TreeNode(7)
# three_7 = TreeNode(6)
# three_8 = TreeNode(5)
# root.left = one_1
# root.right = one_2
# one_1.left = two_1
# one_1.right = two_2
# one_2.left = two_3
# one_2.right = two_4
#
# two_1.left = three_1
# two_1.right = three_2
# two_2.left = three_3
# two_2.right = three_4
# two_3.left = three_5
# two_3.right = three_6
# two_4.left = three_7
# two_4.right = three_8
# lista = [1,2,4,5]
# for i in range(len(lista)-1,0,-1):
#     print(lista[i])
# s = '100'
# print(bin(s))
# import numpy as np
# import math
# p1=np.array([1,10])
# p2=np.array([1000,2000])
# p3=p2-p1
# p4=math.hypot(p3[0],p3[1])
# p5 = np.sqrt(np.sum(np.square(p3)))
# print(p4)
# print(p5)
# list = []
# list[]
# class Student:
#     def __init__(self):  # 两者之间的区别
#         self.name = None
#         self.score = None
#
#     # def __init__(self, name, score):
#     #     self.name = name
#     #     self.score = score
#
#     def print_score(self):
#         print("%s score is %s" % (self.name, self.score))
#
#     def get_grade(self):
#         if self.score >= 80:
#             return "A"
#         elif self.score >= 70:
#             return "B"
#         else:
#             return "C"
#
#
# student = Student("sansan", 90)
# # student = Student()
# # student.name = "sansan"
# # student.score = 90
#
# susan = Student("sunny", 78)
# # susan = Student()
# # susan.name = "susan"
# # susan.score = 8
#
# student.print_score()
# susan.print_score()
# print(susan.get_grade())
# print(student.get_grade())

# class Solution:
#     def Fibonacci(self, n):
#         # write code here
#         if n <= 1:
#             return 1
#         res = [0] * n
#         res[0] = 1
#         res[1] = 1
#         i = 2
#         while i < n:
#             res[i] = res[i-1] + res[i-2]
#             i += 1
#         return res[-1]
# s = Solution()
# n = 0
# print(s.Fibonacci(n))
# n = -4
# m = str(bin(n))
# print(m)
# print(m.count('1'))
# -*- coding:utf-8 -*-
# class Solution:
#     def reOrderArray(self, array):
#         # write code here
#         if len(array) == 1:
#             return array
#         l = len(array)
#         i = 0
#         odd_count = 0
#         even_count = 0
#
#         while (odd_count + even_count) < l:
#             if array[i] & 1:
#                 i += 1
#                 odd_count += 1
#             else:
#                 array.append(array[i])
#                 array.pop(i)
#                 even_count += 1
#         return array
# s = Solution()
# nums = [1,2,3,2,3,4,5,4,5,6]
# print(s.reOrderArray(nums))
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution:
#     # 返回合并后列表
#     def Merge(self, pHead1, pHead2):
#         # write code here
#         if pHead1 is None and pHead2 is None:
#             return None
#         elif pHead1 and pHead2 is None:
#             return pHead1
#         elif pHead1 and pHead1 is None:
#             return pHead2
#         p1 = pHead1
#         p2 = pHead2
#         p3 = ListNode(0)
#         temp = p3
#         while p1 and p2:
#             if p1.val < p2.val:
#                 p3 = p1
#                 p1 = p1.next
#                 p3 = p3.next
#             elif p1.val > p2.val:
#                 p3 = p2
#                 p1 = p2.next
#                 p3 = p3.next
#             else:
#                 p3 = p1
#                 p1 = p1.next
#                 p3.next = p2
#                 p2 = p2.next
#                 p3 = p3.next.next
#         if p2:
#             p3 = p2
#
#         if p1:
#             p3 = p1
#         return temp
#
# s  = Solution()
# p1 = ListNode(1)
# p2 = ListNode(3)
# p3 = ListNode(5)
# p4 = ListNode(7)
# p5 = ListNode(8)
# p6 = ListNode(9)
# p1.next = p2
# p2.next = p3
# p3.next = p4
# p4.next = p5
# p5.next = p6
#
# p7 = ListNode(1)
# p8 = ListNode(2)
# p9 = ListNode(2)
#
# p7.next = p8
# p8.next = p9
# print(s.Merge(p1, p7))
# -*- coding:utf-8 -*-
# class Solution:
#     def __init__(self):
#         self.stack1 = []
#         self.minstack = []
#
#     def push(self, node):
#         # write code here
#         self.stack1.append(node)
#         if self.minstack is None or node <= self.minstack[-1]:
#             self.minstack.append(node)
#
#     def pop(self):
#         # write code here
#         if self.minstack[-1] == self.stack1[-1]:
#             self.minstack.pop()
#         self.stack1.pop()
#
#     def top(self):
#         # write code here
#         return self.stack1[-1]
#
#     def min(self):
#         # write code here
#         return self.minstack[-1]

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# class Solution:
#     # 返回二维列表，内部每个列表表示找到的路径
#     def FindPath(self, root, expectNumber):
#         # write code here
#         if root is None:
#             return None
#         res = []
#
#         def hasPath(root, temp, num):
#             temp.append(root.val)
#             num -= root.val
#             if num == 0 and root.left is None and root.right is None:
#                 # cur = []
#                 # for i in temp:
#                 #     cur.append(temp.val)
#
#                 res.append(temp)
#             if root.left:
#                 hasPath(root.left, temp, num)
#             if root.right:
#                 hasPath(root.right, temp, num)
#             temp.pop()
#         hasPath(root, [], expectNumber)
#         return res
# class Solution:
#     # 返回二维列表，内部每个列表表示找到的路径
#     def FindPath(self, root, expectNumber):
#         # write code here
#         if not root:
#             return []
#
#         result = []
#
#         def FindPathMain(root, path, currentSum):
#             currentSum += root.val
#
#             path.append(root)
#             isLeaf = root.left == None and root.right == None
#
#             if currentSum == expectNumber and isLeaf:
#                 onePath = []
#                 for node in path:
#                     onePath.append(node.val)
#                 result.append(onePath)
#             if currentSum < expectNumber:
#                 if root.left:
#                     FindPathMain(root.left, path, currentSum)
#                 if root.right:
#                     FindPathMain(root.right, path, currentSum)
#             path.pop()
#
#         FindPathMain(root, [], 0)
#
#         return result
# s = Solution()
# root = TreeNode(1)
# one_1 = TreeNode(2)
# one_2 = TreeNode(5)
# two_1 = TreeNode(1)
# two_2 = TreeNode(8)
# two_3 = TreeNode(2)
# two_4 = TreeNode(5)
# # three_1 = TreeNode(5)
# # three_2 = TreeNode(6)
# # three_3 = TreeNode(7)
# # three_4 = TreeNode(8)
# # three_5 = TreeNode(8)
# # three_6 = TreeNode(7)
# # three_7 = TreeNode(6)
# # three_8 = TreeNode(5)
# root.left = one_1
# root.right = one_2
# one_1.left = two_1
# one_1.right = two_2
# one_2.left = two_3
# one_2.right = two_4
#
# # two_1.left = three_1
# # two_1.right = three_2
# # two_2.left = three_3
# # two_2.right = three_4
# # two_3.left = three_5
# # two_3.right = three_6
# # two_4.left = three_7
# # two_4.right = three_8
#
# n = 11
# print(s.FindPath(root, n))
# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution:
#     def deleteDuplication(self, pHead):
#         first = ListNode(-1)
#         first.next = pHead
#         curr = pHead
#         last = first
#         while curr and curr.next:
#             if curr.val != curr.next.val:
#                 curr = curr.next
#                 last = last.next
#             else:
#                 val = curr.val
#                 while curr and curr.val == val:
#                     curr = curr.next
#                 last.next = curr
#         return first.next
# s = Solution()
# node = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(2)
# node4 = ListNode(3)
# node5 = ListNode(4)
# node6 = ListNode(4)
# node.next = node2
# node2.next = node3
# node3.next = node4
# node4.nxt = node5
# node5.next = node6
# a = s.deleteDuplication(node)
# while a:
#     print(a.val)
#     a = a.next
# # print(s.deleteDuplication(node))
# import copy
# l1 = [1, 2, 3, [11, 22, 33]]
# l3 = copy.copy(l1)#  浅拷贝
# print(l1,'>>>',l3)
# l3[0] =10
# print(l1,'>>>',l3)
# l2 = copy.deepcopy(l1)
# print(l1,'>>>',l2)
# l2[3][0] = 1111
# print(l1,">>>",l2)
class Soultion():
    def window(self, nums, size):
        if size > len(nums) or len(nums) == 0:
            return None
        temp = [0]
        res = []
        for i in range(len(nums)):
            if i - temp[0] > size-1:
                temp.pop(0)
            while len(temp) > 0 and nums[i] >= nums[temp[-1]]:
                temp.pop()
            if len(temp) < size-1:
                temp.append(i)
            if i >= size-1:
                res.append(temp[0])
        return res

