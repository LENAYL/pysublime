# 用队列实现
#
# from queue import Queue
# class MyStack(object):
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.q1 = Queue()
#         self.q2 = Queue()
#
#     def push(self, x):
#         """
#         Push element x onto stack.
#         :type x: int
#         :rtype: void
#         """
#         self.q1.put(x)
#
#     def pop(self):
#         """
#         Removes the element on top of the stack and returns that element.
#         :rtype: int
#         """
#         while self.q1.qsize() > 1:
#             self.q2.put(self.q1.get())
#         if self.q1.qsize() == 1:
#             res = self.q1.get()
#             temp = self.q2
#             self.q2 = self.q1
#             self.q1 = temp
#             return res
#
#
#     def top(self):
#         """
#         Get the top element.
#         :rtype: int
#         """
#         while self.q1.qsize() > 1:
#             self.q2.put(self.q1.get())
#         if self.q1.qsize() == 1:
#             res = self.q1.get()
#             self.q2.put(res)    # 将q1最后的一个元素存入q2  此时 q2 == 原来的q1
#             tem = self.q2
#             self.q2 = self.q1
#             self.q1 = tem
#             return res
#
#     def empty(self):
#         """
#         Returns whether the stack is empty.
#         :rtype: bool
#         """
#         return self.q1.qsize() != 0
#
# # Your MyStack object will be instantiated and called as such:
# # obj = MyStack()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.empty()


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self,q1 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        self.q1.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q1[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.q1 != 0)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()