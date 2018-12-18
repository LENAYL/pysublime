# class MinStack(object):
    # method 2
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.sorted_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.sorted_stack) == 0 or x < self.sorted_stack[-1]:
            self.sorted_stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        top = self.stack.pop()
        if top == self.sorted_stack[-1]:
            self.sorted_stack.pop()
        return top

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.sorted_stack[-1]











    # method 1
    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.items = []
    #     self.min = None
    #
    # def push(self, x):
    #     """
    #     :type x: int
    #     :rtype: void
    #     """
    #     self.items.append(x)
    #     if self.min is None or self.min > x:
    #         self.min = x
    #
    # def pop(self):
    #     """
    #     :rtype: void
    #     """
    #     top = self.items.pop()
    #     if len(self.items) == 0:
    #         self.min = None
    #         return top
    #     if top == self.min:
    #         for i in range(len(self.items)):
    #             if self.items[i] < self.min:
    #                 self.min = self.items[i]
    #         return top
    #
    #
    #
    # def top(self):
    #     """
    #     :rtype: int
    #     """
    #     return self.items[len(self.items)-1]
    #
    # def getMin(self):
    #     """
    #     :rtype: int
    #     """
    #     return self.min
        # 又超时啦 大辣鸡
        # if len(self.items) == 0:
        #     return None
        # if len(self.items) == 1:
        #     return self.items[0]
        # min = self.items[0]
        # # self.items[len(self.items)]
        # # while len(self.items):
        # for i in range(len(self.items)):
        #     if min > self.items[i]:
        #         min = self.items[i]
        # return min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
