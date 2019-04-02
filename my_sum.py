#Author: Lena
#data:2019/4/2 15:49
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.sum = 0
    def Sum_Solution(self, n):
        # write code here
        self.sum += n
        n -= 1
        if n:
            self.Sum_Solution(n)
        return self.sum
s = Solution()
num = 10
print(s.Sum_Solution(num))